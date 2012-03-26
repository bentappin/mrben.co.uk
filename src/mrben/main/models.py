import uuid

from django.db import models
from django.contrib.auth.models import User

from mrben.main.managers import PublicManager


class Category(models.Model):
    """Category model."""

    title = models.CharField(max_length=40)
    slug = models.SlugField()

    def get_absolute_url(self):
        return "/category/%s/" % self.slug

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')
        ordering = ['title']


class Entry(models.Model):
    """Entry model."""
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (  (LIVE_STATUS, 'Live'),
                              (DRAFT_STATUS, 'Draft'),
                              (HIDDEN_STATUS, 'Hidden'),
                              )

    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=False, null=False, unique=True)
    author = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField()
    body_highlighted = models.TextField(blank=True, null=True)
    allow_comments = models.BooleanField(default=True)
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    guid = models.CharField(max_length='36', blank=False, null=False)
    objects = PublicManager()

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return "/entry/%s/" % self.slug

    def unescape_html(self, html):
        html = html.replace('&lt;', '<')
        html = html.replace('&gt;', '>')
        html = html.replace('&amp;', '&')
        return html

    def highlight_code(self, html):
        """ Highlight code snippets. Based on:
            http://www.saltycrane.com/blog/2008/08/django-blog-project-12-adding-pygments-syntax-highlighting/ """

        from BeautifulSoup import BeautifulSoup
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name
        from pygments.formatters import HtmlFormatter

        soup = BeautifulSoup(html)
        preblocks = soup.findAll('pre')
        for pre in preblocks:
            if pre.has_key('class'):
                try:
                    code = ''.join([unicode(item) for item in pre.contents])
                    code = self.unescape_html(code)
                    lexer = get_lexer_by_name(pre['class'])
                    formatter = HtmlFormatter()
                    code_hl = highlight(code, lexer, formatter)
                    pre.replaceWith(BeautifulSoup(code_hl))
                except:
                    pass
        return unicode(soup)

    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = str(uuid.uuid4())
        self.body_highlighted = self.highlight_code(self.body)
        super(Entry, self).save(*args, **kwargs)

    class Admin:
        list_display = ('title', 'publish', 'status')
        list_filter = ('publish', 'categories', 'status')
        search_fields = ('title', 'body')

    class Meta:
        ordering = ['-publish']
        verbose_name_plural = 'entries'


class Link(models.Model):
    """Link model."""
    title = models.CharField(max_length=50)
    url = models.URLField()

    def __unicode__(self):
        return u'%s - %s' % (self.title, self.url)

    class Meta:
        ordering = ['title']

from django.db import models
from django.contrib.auth.models import User

from mrben.main.managers import PublicManager


class Category(models.Model):
	"""Category model."""
	title = models.CharField(max_length=40)
	
	def get_absolute_url(self):
		return "/category/%s/" % self
	
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
	STATUS_CHOICES = (	(LIVE_STATUS, 'Live'),
						(DRAFT_STATUS, 'Draft'),
						(HIDDEN_STATUS, 'Hidden'),
	)
	
	title = models.CharField(max_length=40)
	slug = models.SlugField(blank=True)
	author = models.ForeignKey(User, blank=True, null=True)
	body = models.TextField()
	teaser = models.TextField()
	allow_comments = models.BooleanField(default=True)
	publish = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField(Category, blank=True, null=True)
	status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
	objects = PublicManager()
	
	def __unicode__(self):
		return u'%s' % self.title
		
	def get_absolute_url(self):
		return "/entry/%i/" % self.id
		
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
		ordering =  ['title']

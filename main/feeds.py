from django.contrib.syndication.views import Feed
from mrben.main.models import Entry


class EntriesFeed(Feed):
    title = "mrben.co.uk | web developer and tinkerer"
    link = '/'
    description = "The personal blog of Ben Tappin - web developer and tinkerer."

    def items(self):
        return Entry.objects.published().exclude(categories__title='Projects').exclude(categories__title='Portfolio')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
        
    def item_link(self, item):
        return item.get_absolute_url()
        
    def item_author_name(self, item):
        return item.author.get_full_name() or item.author.username
        
    def item_pubdate(self, item):
        return item.publish
        
    def item_author_email(self, item):
        return item.author.email
    
    def item_guid(self, item):
        return u'%s' % item.pk
        
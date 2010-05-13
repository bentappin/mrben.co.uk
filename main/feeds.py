from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404

from mrben.main.models import Entry, Category


class EntriesFeed(Feed):
    title = "mrben.co.uk | web developer and tinkerer"
    link = '/feed/'
    description = "The personal blog of Ben Tappin - web developer and tinkerer."
    feed_type = Atom1Feed

    def items(self):
        return Entry.objects.published().exclude(categories__slug='portfolio')

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
        return item.guid
        
    def item_categories(self, item):
        return [c.title for c in item.categories.all()]


class CategoriesFeed(EntriesFeed):
    def get_object(self, request, category_slug):
        return get_object_or_404(Category, slug=category_slug)
    
    def items(self, obj):
        return Entry.objects.published().filter(categories=obj)
    
    def title(self, obj):
        return "mrben.co.uk - entries in the %s category" % obj
    
    def link(self, obj):
        return obj.get_absolute_url()
    
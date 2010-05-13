from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.conf import settings

from mrben.main.models import Entry, Category


class EntriesFeed(Feed):
    title = "mrben.co.uk | web developer and tinkerer"
    link = '/feed/'
    description = "The personal blog of Ben Tappin - web developer and tinkerer."
    feed_type = Atom1Feed

    def items(self):
        entries = cache.get('entries')
        
        if entries is None:
            entries = Entry.objects.published().exclude(categories__slug='portfolio')
            cache.set('entries', entries, settings.FEED_CACHE_TIMEOUT)
            
        return entries

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
        cache_key = 'entries %s' % obj.slug
        entries = cache.get(cache_key)

        if entries is None:
            entries = Entry.objects.published().filter(categories=obj)
            cache.set(cache_key, entries, settings.FEED_CACHE_TIMEOUT)
        
        return entries
    
    def title(self, obj):
        return "mrben.co.uk - entries in the %s category" % obj
    
    def link(self, obj):
        return obj.get_absolute_url()
    
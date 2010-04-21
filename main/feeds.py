from django.contrib.syndication.views import Feed
from main.models import Entry


class EntriesFeed(Feed):
    title = "mrben.co.uk"
    link = '/'
    description = "mrben | web developer and tinkerer"

    def items(self):
        return Entry.objects.published().exclude(categories__title='Projects').exclude(categories__title='Portfolio')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser
        
    def item_link(self, item):
        return item.get_absolute_url()
    
from django.contrib.syndication.views import Feed
from apps.data.models import Entry

class ArchiveFeed(Feed):

    title = 'Archive Feed'
    description = 'Archive Feed'
    link = '/archive/'

    def items(self):
        return Entry.objects.published_entries()[:25]

    def item_title(self,item):
        return item.title

    def item_link(self,item):
        return self.link

    def item_description(self,item):
        return item.text


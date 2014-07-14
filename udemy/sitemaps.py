from django.contrib.sitemaps import Sitemap
from apps.data.models import Entry

class BlogSitemap(Sitemap):
    priority = None
    changefreq = None

    def items(self):
        return Entry.objects.all()

    def lastmod(self, item):
        return item.updated

    def location(self, item):
        return ''

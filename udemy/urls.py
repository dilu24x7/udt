from udemy import settings
from django.conf.urls import patterns, include, url
from sitemaps import BlogSitemap

sitemaps = {
    'blog':BlogSitemap
    }

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.homepage.urls')),
    url(r'^', include('apps.accounts.urls')),
    # Examples:
    # url(r'^$', 'udemy.views.home', name='home'),
    # url(r'^udemy/', include('udemy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^sitemap\.xml','django.contrib.sitemaps.views.sitemap',{'sitemaps':sitemaps}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*$)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT})
)

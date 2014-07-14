from django.conf.urls import patterns, include, url
from apps.homepage.feeds import ArchiveFeed

urlpatterns = patterns('apps.homepage.views',
url(r'^$','index',name='homepage'),
url(r'^about/$','about',name='homepage_about'),
url(r'^contact/$','contact',name='homepage_contact'),
)

urlpatterns += patterns('',
    (r'^feed/archive/$',ArchiveFeed()),
    )

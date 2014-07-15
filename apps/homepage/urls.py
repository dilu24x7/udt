from django.conf.urls import patterns, include, url
from apps.homepage.feeds import ArchiveFeed
from django.contrib.auth.views import login,logout

urlpatterns = patterns('apps.homepage.views',
url(r'^$','index',name='homepage'),
url(r'^about/$','about',name='homepage_about'),
url(r'^contact/$','contact',name='homepage_contact'),
url(r'^profile/$','profile',name='homepage_profile'),
)

urlpatterns += patterns('',
    url(r'^login/$',login,kwargs={'template_name':'homepage/login.html'},name='homepage_login'),
    url(r'^logout/$',logout,kwargs={'next_page':'/'},name='homepage_logout'),
    (r'^feed/archive/$',ArchiveFeed()),
    )

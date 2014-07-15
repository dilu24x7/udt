from django.conf.urls import patterns,include,url
from django.contrib.auth.views import login,logout

urlpatterns = patterns('',
    url(r'^login/$',login,kwargs={'template_name':'accounts/login.html'},name='accounts_login'),
    url(r'^logout/$',logout,kwargs={'next_page':'/'},name='accounts_logout'),
    url(r'^profile/$','apps.accounts.views.profile',name='accounts_profile'),
    url(r'^register/$','apps.accounts.views.register',name='accounts_register')
    )

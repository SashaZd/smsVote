from django.conf.urls import patterns, include, url
from django.contrib import admin

from manager import UserManager, BoothManager

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smsVote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api/user/$', UserManager.userRequest, name='userrequest'),
    url(r'^api/user/(?P<user_id>\d*)/$', UserManager.userRequest, name='userGet'),
    
    url(r'^api/booth/$', BoothManager.boothRequest, name='boothrequest'),
    url(r'^api/booth/(?P<booth_id>\d*)/$', BoothManager.boothRequest, name='boothGet'),
    
    url(r'^api/booth/(?P<booth_id>\d*)/sms/$', BoothManager.boothSMS, name='boothSMS')
)

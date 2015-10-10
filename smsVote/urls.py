from django.conf.urls import patterns, include, url
from django.contrib import admin

from manager import UserManager, BoothManager

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smsVote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api/user/$', UserManager.userRequest, name='userrequest'),
    
    url(r'^api/booth/$', BoothManager.boothRequest, name='boothrequest'),
    
    url(r'^api/booth/sms/$', BoothManager.boothSMS, name='boothrequest')
)

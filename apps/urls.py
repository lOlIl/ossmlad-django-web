from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'event.views.home'),
    url(r'^event/$', 'event.views.index'),
    url(r'^event/(?P<event_id>\d+)/$', 'event.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)

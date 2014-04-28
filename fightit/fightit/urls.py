from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fightit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'fightit.views.home', name='home'),
    url(r'^ui/$', 'ui.views.home', name='ui-home'),

    url(r'^admin/', include(admin.site.urls)),
)

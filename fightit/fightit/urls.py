from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fightit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'fightit.views.home', name='home'),
    url(r'^ui/$', 'ui.views.ui', name='ui-ui'),
    url(r'^ui/table/$', 'ui.views.table', name='ui-table'),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ejercicios.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cms/nuevo/(.*)/(.*)', 'cms.views.nuevo'),
    url(r'^cms/show/$', 'cms.views.show'),
    url(r'^admin/', include(admin.site.urls)),
)

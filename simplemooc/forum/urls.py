from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.forum.views',
    
    url(r'^$', 'index', name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', 'index', name='index_tagged'),
    url(r'^topico/(?P<slug>[\w_-]+)/$', 'thread', name='thread'),
)
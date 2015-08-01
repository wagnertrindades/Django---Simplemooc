from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.forum.views',
    
    url(r'^$', 'index', name='index'),
)
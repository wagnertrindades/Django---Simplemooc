from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    # Url com primary key
    #url(r'^(?P<pk>\d+)$', 'details', name='details'),
    
    # Url com slug
    url(r'^(?P<slug>[\w_-]+)$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', 'enrollment', name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', 'announcements', name='announcements'),
)
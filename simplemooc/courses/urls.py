from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    # Url com primary key
    #url(r'^(?P<pk>\d+)$', 'details', name='details'),
    
    # Url com slug
    url(r'^(?P<slug>[\w_-]+)$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', 'enrollment', name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', 'undo_enrollment', name='undo_enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', 'announcements', name='announcements'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', 'show_announcement', name='show_announcement'),
    url(r'^(?P<slug>[\w_-]+)/aulas/$', 'lessons', name='lessons'),
    url(r'^(?P<slug>[\w_-]+)/aula/(?P<pk>\d+)/$', 'show_lesson', name='show_lesson'),
    url(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', 'material', name='material'),
)
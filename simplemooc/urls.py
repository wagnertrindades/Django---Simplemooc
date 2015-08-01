from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^conta/', include('simplemooc.accounts.urls', namespace='accounts')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^forum/', include('simplemooc.forum.urls', namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
)

# Se estiver em ambiente de desenvolvimento DEBUG o static pega a url base e pega o arquivo pelo document root
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
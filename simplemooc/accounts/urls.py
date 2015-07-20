from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'simplemooc.accounts.views.dashboard', name='dashboard'),
    url(r'^entrar/$', 'django.contrib.auth.views.login', 
        {'template_name' : 'accounts/login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', 
        {'next_page' : 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', 'simplemooc.accounts.views.register', name='register'),
    url(r'^nova-senha/$', 'simplemooc.accounts.views.password_reset', name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', 
        'simplemooc.accounts.views.password_reset_confirm', 
        name='password_reset_confirm'),
    url(r'^editar/$', 'simplemooc.accounts.views.edit', name='edit'),
    url(r'^editar-senha/$', 'simplemooc.accounts.views.edit_password', name='edit_password'),
)
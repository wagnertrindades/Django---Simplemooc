from django.shortcuts import render
from django.views.generic import TemplateView, View

# Class-Based Views

# Template view tem a proposta de renderizar apenas o template,
# Não vamos utilizar porque não queremos apenas renderizar o template
# Queremos listar os modelos
# A Template View é uma Generic View que herda da View que é a base das generics views

# Formas de utilizar o TemplateView
# 1 
# class ForumView(TemplateView):

#     template_name = 'forum/index.html'

# index = ForumView.as_view()

# 2
# index = TemplateView.as_view(template_name='forum/index.html')

# Vamos utilizar a View porque a ideia da ForumView é listar os modelos
class ForumView(View):

    def get(self, resquest, *args, **kwargs):
        return render(resquest, 'forum/index.html')

index = ForumView.as_view()

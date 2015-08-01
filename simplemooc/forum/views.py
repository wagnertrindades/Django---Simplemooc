from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView

from .models import Thread

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

# A view padrão mostra o modelo
# A View padrão pode ser implementada assim
# class ForumView(View):

#     def get(self, resquest, *args, **kwargs):
#         return render(resquest, 'forum/index.html')

# index = ForumView.as_view()

# ListView
class ForumView(ListView):

    model = Thread
    paginate_by = 10
    template_name = 'forum/index.html'

index = ForumView.as_view()
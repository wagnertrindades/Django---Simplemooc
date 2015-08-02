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

    paginate_by = 2
    template_name = 'forum/index.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        # Quando usamos os parametros pela url no caso Tag, 
        # utilizamos para parametros não nomeados o *args
        # E **kwargs para parametros nomeados
        tag = self.kwargs.get('tag', '')
        if tag:
            queryset = queryset.filter(tags__slug__icontains=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context

index = ForumView.as_view()
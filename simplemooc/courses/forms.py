from django import forms
from django.core.mail import send_mail
from django.conf import settings 

from simplemooc.core.mail import send_mail_template

from .models import Comment

class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    #Envio de email simples
    #
    # def send_mail(self, course):
    #     subject = '[%s] Contato' % course
    #     # Passando na string como nomeada pode se inserir um dicionario que no caso é o context 
    #     message = 'Nome: %(name)s; Email: %(email)s; Messagem: %(message)s'
    #     context = {
    #         'name' : self.cleaned_data['name'],
    #         'email' : self.cleaned_data['email'],
    #         'message' : self.cleaned_data['message'],
    #     }
    #     message = message % context
    #     # Chama a função send_mail do django.core.mail importada lá em cima e passa o subject, message, email que vai enviar a messagem, email a ser enviado
    #     send_mail(
    #         subject, message, settings.DEFAULT_FROM_EMAIL, 
    #         [settings.CONTACT_EMAIL]
    #     )

    #Envio de mail completo
    def send_mail(self, course):
        subject = '[%s] Contato' % course
        context = {
            'name' : self.cleaned_data['name'],
            'email' : self.cleaned_data['email'],
            'message' : self.cleaned_data['message'],
        }
        template_name = 'courses/contact_email.html'
        # Chama a função send_mail_template que foi definida no core do projeto simplemooc
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
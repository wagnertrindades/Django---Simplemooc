from django import forms
from django.core.mail import send_email
from django.conf import settings 

class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_email(self, course):
        subject = '[%s] Contato' % course
        # Passando na string como nomeada pode se inserir um dicionario que no caso é o context 
        message = 'Nome: %(name)s; Email: %(email)s; Messagem: %(message)s'
        context = {
            'name' : self.cleaned_data['name'],
            'email' : self.cleaned_data['email'],
            'message' : self.cleaned_data['message'],
        }
        message = message % context
        # Chama a função send_email do django.core.mail importada lá em cima e passa o subject, message, email que vai enviar a messagem, email a ser enviado
        send_email(
            subject, message, settings.DEFAULT_FROM_EMAIL, 
            [settings.CONTACT_EMAIL]
        )
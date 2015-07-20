import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):
    """
    Usuário Custom - Herda do AbstractBaseUser e PermissionsMixin assim como o User padrão do django

    A diferença é que aqui configuramos o nosso model diferente do padrão do django,
    Quando o padrão do django não atende o modelo de usuário utilizamos um custom
    """
    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True, 
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    # Unique é para ser um email unico
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    # Adiciona o UserManager que tem coisas uteis para o user
    objects = UserManager()

    # Indica o campo que é unico e é a referencia na hora de login
    USERNAME_FIELD = 'username'
    # É utilizado no comando de criação de superusuário
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return "{0} em {1}".format(self.user, self.created_at)

    class Meta:
        verbose_name ='Nova Senha'
        verbose_name_plural ='Novas Senhas'
        ordering = ['-created_at']
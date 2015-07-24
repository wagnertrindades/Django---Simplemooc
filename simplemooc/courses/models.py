from django.db import models
from django.conf import settings
from django.utils import timezone

from simplemooc.core.mail import send_mail_template

class CourseManager(models.Manager):
	"""
		Class para adicionar um select customizado do BD
		Utilizando o Manager do models
	"""

	def search(self, query):
		"""
			Metodo que filtra o que é digitado como query
			No name ou description
		"""
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query)
		)


class Course(models.Model):
	"""
		Class contendo os cursos 

		OBS: 
		Os nome entre '' são verbose names = nomes amigaveis para o usuário

		blank=True -> significa que o campo não é obrigatório
		null=True -> significa que ele pode retornar como none
		upload_to -> pega o caminho do MEDIA_ROOT e aciona o caminho informado
		auto_now_add -> Adiciona a data do qual foi Criado
		auto_now -> Adiciona a data toda vez que salva

	"""
	# Strings com max length
	name = models.CharField('Nome', max_length=100)
	# Slug é um nome unico, sem espacos e em minusculas
	slug = models.SlugField('Atalho')
	# TextField é um campo de strings sem max length
	description = models.TextField('Descrição Simples', blank=True)
	about = models.TextField('Sobre o curso', blank=True)
	# DateField pegada a data
	start_date = models.DateField(
		'Data de Início', null=True, blank=True
	)
	# Image Field Armazena o caminho da imagem
	image = models.ImageField(
		upload_to='courses/images', verbose_name='Imagem', null=True, blank=True
	)
	# DateTimeField pega data e horario
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	# Insere o select customizado CourseManager no objects do django
	objects =  CourseManager()

	def __str__(self):
		"""
			Coloca o name como "Apelido" ao objeto quando referenciado no admin do django
		"""
		return self.name

	# O models.permalink faz o from django.core.urlresolvers import reverse para resgatar o link conforme a função que é feita abaixo	
	@models.permalink
	def get_absolute_url(self):
		"""
			Faz um permalink para o objeto
		"""
		return ('courses:details', (), { 'slug' : self.slug })

	def release_lessons(self):
		today = timezone.now().date()
		# release_date__gte -> filtro se é maior ou igual
		return self.lessons.filter(release_date__gte=today)

	class Meta:
		"""
			A classe meta serve para fazer uma customização no verbose name do admin do django da classe Course e também ordenar os campos
		"""
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']

class Lesson(models.Model):

	name = models.CharField('Nome', max_length=100)
	description = models.TextField('Descrição', blank=True)
	number = models.IntegerField('Número (ordem)', blank=True, default=0)
	release_date = models.DateField('Data de Liberação', blank=True, null=True)

	course = models.ForeignKey(Course, verbose_name='Curso', related_name='lessons')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	def is_available(self):
		if self.release_date:
			today = timezone.now().date()
			return self.release_date >= today
		return False

	class Meta:
		verbose_name = 'Aula'
		verbose_name_plural = 'Aulas'
		ordering = ['number']

class Material(models.Model):

	name = models.CharField('Nome', max_length=100)
	embedded = models.TextField('Video embedded', blank=True)
	archive = models.FileField(upload_to='lessons/materials', blank=True, null=True)

	lesson = models.ForeignKey(Lesson, verbose_name='Aula', related_name='materials')

	def is_embedded(self):
		return bool(self.embedded)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Material'
		verbose_name_plural = 'Materiais'

class Enrollment(models.Model):

	STATUS_CHOICES = (
		(0, 'Pendente'),
		(1, 'Aprovado'),
		(2, 'Cancelado'),
	)

	# Faz a relação com o usuário
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='enrollments'
	)
	#Faz a relação com o curso
	course = models.ForeignKey(
		Course, verbose_name='Curso', related_name='enrollments'
	)
	status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=1, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def active(self):
		self.status = 1
		self.save()

	def is_approved(self):
		return self.status == 1

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'
		unique_together = (('user', 'course'),)

class Announcement(models.Model):

	course = models.ForeignKey(
		Course, verbose_name='Curso', related_name='announcements'
	)
	title = models.CharField('Título', max_length=100)
	content = models.TextField('Conteúdo')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Anúncio'
		verbose_name_plural = 'Anúncios'
		ordering = ['-created_at']

class Comment(models.Model):

	announcement = models.ForeignKey(
		Announcement, verbose_name='Anúncio', related_name='comments'
	)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário')
	comment = models.TextField('Comentário')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'
		ordering = ['created_at']

def post_save_announcement(instance, created, **kwargs):
	if created:
		subject = instance.title
		template_name = 'courses/announcement_mail.html'
		context = {
			'announcement': instance
		}
		enrollments = Enrollment.objects.filter(course=instance.course, status=1)
		for enrollment in enrollments:
			recipient_list = [enrollment.user.email]
			send_mail_template(subject, template_name, context, recipient_list)

# Ativa o signal
models.signals.post_save.connect(
	post_save_announcement, sender=Announcement, dispatch_uid='post_save_announcement'
)
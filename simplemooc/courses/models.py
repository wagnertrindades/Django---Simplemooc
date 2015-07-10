from django.db import models

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

	class Meta:
		"""
			A classe meta serve para fazer uma customização no verbose name do admin do django da classe Course e também ordenar os campos
		"""
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']
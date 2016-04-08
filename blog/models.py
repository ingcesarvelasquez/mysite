from django.db import models
from django.utils import timezone

class Post(models.Model):
#https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types
	categorias_post = ( 
		('Tech','Tecnologia'),
		('Life', 'Vida y Estilo'),
		('Gral', 'General'),
		)
	categoria_post = models.CharField(max_length=30, choices=categorias_post, default='Tech', verbose_name="Categoria de Post")
	author = models.ForeignKey('auth.User')
	title =  models.CharField(max_length=200)
	text =   models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title


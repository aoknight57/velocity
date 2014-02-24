from django.db import models

# Create your models here.
class Post(models.Model):
	text = models.CharField(max_length=10000)
	title = models.CharField(max_length=500, default='title')

	def __str__(self):
		return self.text
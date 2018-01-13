from django.db import models

# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str('{}-{}'.format(self.name,self.email))
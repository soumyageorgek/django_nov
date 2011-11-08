from django.db import models

# Create your models here.
class Comment(models.Model):
	name = models.CharField(max_length=30)
	message = models.CharField(max_length=100)
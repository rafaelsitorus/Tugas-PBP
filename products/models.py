from django.db import models

# Create your models here.
class Product(models.Model):
	name 		= models.CharField(max_length=200)
	price 		= models.IntegerField()
	description = models.TextField()
	quantity 	= models.IntegerField(default=0)
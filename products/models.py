from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
	id 			= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name 		= models.CharField(max_length=200)
	price 		= models.IntegerField()
	description = models.TextField()
	quantity 	= models.IntegerField(default=0)
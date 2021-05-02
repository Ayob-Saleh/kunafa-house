from django.db import models

# Create your models here.


class Kunafa(models.Model):
	
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	offer = models.BooleanField(default=False)


class Baklawa(models.Model):
	
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	offer = models.BooleanField(default=False)
	

class Crunchy_kunafa(models.Model):
	
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	offer = models.BooleanField(default=False)

class Topping(models.Model):
	
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	

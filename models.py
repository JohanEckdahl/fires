from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

class Fire(models.Model):
	
	number = models.IntegerField(blank=False)
	centerX = models.PositiveIntegerField(blank=False)
	centerY = models.PositiveIntegerField(blank=False)
	quality = models.PositiveSmallIntegerField(validators=[MaxValueValidator(3), MinValueValidator(0)])

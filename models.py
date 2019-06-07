from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

class Fire(models.Model):
    
    def __str__(self):
        return "Fire{}".format(self.OBJECTID)
	
    #Skogsstyrelsen Data
    NAMN       = models.CharField(max_length=100, null=True)
    Producent  = models.CharField(max_length=100, null=True)
    GISHektar  = models.IntegerField(null = False)
    Lannamn    = models.CharField(max_length=100, null=True)
    CenterX    = models.FloatField(null = False)
    CenterY    = models.FloatField(null = False)
    Aktualitet = models.CharField(max_length=100, null=True)
    Kommunnamn = models.CharField(max_length=100, null=True)
    Metod      = models.CharField(max_length=100, null=True)
    Kvalitet   = models.CharField(max_length=100, null=True)
    Kommentar  = models.CharField(max_length=100, null=True)
    OBJECTID   = models.IntegerField(null=False)
    Laddatum   = models.DateField(null=False)
    Lopnr      = models.FloatField(null = False)
    shape_STAr = models.FloatField(null = False)
    shape_STLe = models.FloatField(null = False)
    
    #Our own data
    quality    = models.PositiveSmallIntegerField(validators=[MaxValueValidator(3), MinValueValidator(0)], blank = True, null = True)
    summary    = models.TextField(null=True, blank = True)


class Parking(models.Model):
    def __str__(self):
        return "{}, {}".format(self.latitude, self.longitude)

    latitude  = models.FloatField()
    longitude = models.FloatField()


class Site(models.Model):

    type      = (('burnt','burnt'), ('control','control'))
    fire      = models.ForeignKey(Fire, on_delete=models.CASCADE)
    parking   = models.ForeignKey(Parking, on_delete=models.CASCADE, null=True)
    type      = models.CharField(max_length = 25, choices = type)
    latitude  = models.FloatField()
    longitude = models.FloatField()
    rank      = models.PositiveSmallIntegerField()
    walk      = models.IntegerField(null = True)
    comment   = models.TextField(null=True, blank=True)


    def __str__(self):
        return "Fire {}, {} {}".format(self.fire.OBJECTID, self.type, self.rank)



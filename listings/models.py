from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):

    realtor = models.ForeignKey(Realtor, on_delete= models.DO_NOTHING)
    title= models.CharField(max_length = 200 )
    address= models.CharField(max_length = 200 )
    city= models.CharField(max_length = 100 )
    state= models.CharField(max_length = 100 )
    zipcode= models.CharField(max_length = 20 ) 
    description= models.TextField(blank=True ) #Blank oznacza ze jest to pole nieobowiazkowe a reszta bedzie
    price= models.IntegerField()
    bedroom= models.IntegerField()
    bathorooms= models.DecimalField(max_digits=2, decimal_places=1 ) # daje maksymalna wartosc 99 i max jedno miejsce po przecinku
    garage= models.IntegerField(default=0)
    sqft= models.IntegerField()
    lot_size= models.DecimalField(max_digits=5, decimal_places=1)
    photos_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/') 
    photos_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photos_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photos_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photos_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photos_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photos_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateField(default = datetime.now, blank = True )
    
    def __str__(self):
        return self.title #To daje nam info ze glownym fieldem bedzie title
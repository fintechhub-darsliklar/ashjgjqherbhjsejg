from django.db import models

# Create your models here.


class Yozuvchi(models.Model):
    
    ism = models.CharField(max_length=255)
    familya = models.CharField(max_length=255, blank=True, null=True)
    telefon_raqam = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.ism
    


class Post(models.Model):
    title = models.CharField(max_length=233)



    


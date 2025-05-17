from django.db import models

# Create your models here.

from django.db import models

class Tombe(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images_tombes/')
    
    def __str__(self):
        return self.titre
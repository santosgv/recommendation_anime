from datetime import datetime
from django.db import models
from django.db.models.fields import CharField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User



class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'

    def __str__(self) -> str:
        return self.img.url
    
class Recommend(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = datetime.now()
    imagens = models.ManyToManyField(Imagem)
    sobre = models.TextField(max_length=500 ,blank=True)
    texto = models.TextField(max_length=2000, blank=True)
    link = CharField(max_length=1000,blank=True)
    referencias = models.TextField(blank=True, max_length=500)


    def __str__(self):
        return self.titulo
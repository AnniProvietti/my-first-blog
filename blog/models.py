from django.conf import settings    #linhas com from ou import adicionam pedaços de outros arquivos
from django.db import models
from django.utils import timezone

class Post (models.Model):  #essa linha define o modelo - class define objeto e Post é o nome do modelo
    #models.Model significa que Post é um modelo de Django -salva no banco de dados
    #abaixo temos propriedades do objeto
    author = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link para outro modelo
    title = models.CharField(max_length=200) #texto limitado
    text = models.TextField()   #texto sem limite
    created_date = models.DateTimeField(default=timezone.now)   #data e hora
    published_date = models.DateTimeField(blank=True,null=True)
    #método publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__ (self): #convençao usada em Python
        return self.title


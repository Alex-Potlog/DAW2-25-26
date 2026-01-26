from django.db import models

# Create your models here.


class Autor(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    data_naixement = models.DateField()


class Article(models.Model):
    titol = models.CharField(max_length=200)
    contingut = models.TextField()
    data_publicacio = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name='articles')

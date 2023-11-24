from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Jogador(models.Model):
    name = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=200, null=True)
    categories = models.ManyToManyField(Category)
    release_year = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    jogadores = models.ManyToManyField(Jogador)

    def __str__(self):
        return f'{self.name} by {self.author}'

class Provider(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    service = models.CharField(max_length=255, blank=True)
    has_flat_price = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.service} @ {self.price if self.price else "flat"}'

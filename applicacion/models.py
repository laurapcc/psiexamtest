from django.db import models


class Usuario(models.Model):
    """Model representing an user."""
    username = models.CharField(max_length=100)


class Tweet(models.Model):
    """Model representing a tweet."""
    texto = models.CharField(max_length=144)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()


class Retweet(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    fechaDeRetweet = models.DateField()
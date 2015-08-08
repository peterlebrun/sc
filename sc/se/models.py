from django.db import models
import datetime

# Create your models here.

class Pillar(models.Model):
    content = models.TextField()

class Prompt(models.Model):
    content = models.TextField()
    pillar  = models.ForeignKey(Pillar, null=True)
    week    = models.IntegerField(default=None, null=True)
    date    = models.DateTimeField(default=None)

class Response(models.Model):
    content = models.TextField()
    prompt  = models.ForeignKey(Prompt)
    date    = models.DateTimeField(default=None)

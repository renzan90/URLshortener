from django.db import models

#Create your models here

class URL(models.Model):
    original_url = models.URLField(max_length=20)
    shorter = models.TextField(max_length=20, primary_key=True)

def __str__(self):
    return self.original_url
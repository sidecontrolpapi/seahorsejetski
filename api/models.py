from django.db import models

# Create your models here.

class Review(models.Model):
     name = models.CharField(max_length=150)
     message = models.TextField()

class Message(models.Model):
     email = models.EmailField(max_length=150)
     message = models.TextField()
    

def __str__(self):
    return self.email
 
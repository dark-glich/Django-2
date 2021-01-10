from django.db import models

class comments(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=245) 
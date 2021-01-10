from django.db import models
from datetime import date 
from django.urls import reverse

class post(models.Model):
    title = models.CharField(max_length=60)
    subtitle_1 = models.CharField(max_length=50)
    para_1 = models.TextField()
    subtitle_2 = models.CharField(max_length=50, blank=True)
    para_2 = models.TextField(blank=True)
    description = models.CharField(max_length=300, default="none")
    image = models.ImageField(blank=True, null=True, upload_to='image/')
    creator = models.CharField(max_length=30)
    date = models.DateField(default=date.today())

    def get_absolute_url(self):
        return reverse('article', kwargs={'my_id' :self.id })
    
    def get_absolute_url_2(self):
        return reverse('article', kwargs={'my_id' :self.id +1})


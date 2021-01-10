from django.db import models
from django.urls import reverse

class form(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=245)
    password = models.CharField(max_length=40)
    terms_condition = models.BooleanField("I agree to terms and conditions", default=True, blank=True)

    def get_absolute_url(self):
        return reverse('signin')

from django.db import models


class Tutorial(models.Model):
    id_test = models.CharField(max_length=70, blank=False, default='')
    name = models.CharField(max_length=200, blank=False, default='')
    email = models.CharField(max_length=200, blank=False, default='')
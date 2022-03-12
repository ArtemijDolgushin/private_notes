from django.conf import settings
from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.TextField(verbose_name='Text')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Created by')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created on')

    class Meta:
        verbose_name_plural = 'Notes'
        verbose_name = 'Note'
        ordering = ['-created']


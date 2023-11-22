from django.db import models

class RandomQuotes(models.Model):
    author = models.CharField(verbose_name='автор', max_length=100, blank=True, null=True)
    body = models.CharField(verbose_name='цитата', max_length=255, blank=True, null=True)

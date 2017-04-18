from __future__ import unicode_literals

from django.db import models

class Snippet(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

# Create your models here.

from django.db import models

# Create your models here.
class Msafiri(models.Model):
	msafiri_title = models.CharField(max_length=200)
	msafiri_description = models.TextField()
	msafiri_time = models.DateTimeField("Day signed in")

	def ___str__(self):
		return self.msafiri_title
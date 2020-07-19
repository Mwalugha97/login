from django.db import models


class MsafiriCategory(models.Model):
	msafiri_category = models.CharField(max_length=200)
	msafiri_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.msafiri_category


class MsafiriDetails(models.Model):
	msafiri_details = models.CharField(max_length=200)
	msafiri_category = models.ForeignKey(MsafiriCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Details"

	def __str__(self):
		return self.msafiri_details


# Create your models here.
class Msafiri(models.Model):
	msafiri_title = models.CharField(max_length=200)
	msafiri_description = models.TextField()
	msafiri_time = models.DateTimeField("Day signed in")

	msafiri_details = models.ForeignKey(MsafiriDetails, default=1, verbose_name="Details", on_delete=models.SET_DEFAULT)
	msafiri_slug = models.CharField(max_length=200, default=1)



	def ___str__(self):
		return self.msafiri_title
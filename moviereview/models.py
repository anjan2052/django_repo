from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=100)
	release_year = models.DateField(blank=True,null=True)
	poster = models.ImageField(blank=True,null=True,upload_to="posters/")
	review = models.TextField(null=True)

	def __str__(self):
		return self.title


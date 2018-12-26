from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BlogArticles(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=30)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ("-publish",)
		

	
		

			

		


# Create your models here.

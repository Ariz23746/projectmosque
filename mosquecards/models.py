from django.db import models

from django.db import models
from datetime import datetime


class mosquecards(models.Model):

	image = models.ImageField(upload_to='images/')
	MosqueName = models.CharField(max_length=200, default='')
	address = models.CharField(max_length=200, default='')
	mosqueBanner = models.ImageField(upload_to='images/',default='')
	hadithOfTheDay = models.TextField(default='', blank=True)
	ispublished = models.BooleanField(default=False)
	fajr = models.TimeField()
	zuhar = models.TimeField()
	asar = models.TimeField()
	maghrib = models.TimeField()
	isha = models.TimeField()


	

	def ShortAddress(self):

		return self.address[:40]

	def __str__(self):
		return self.MosqueName
		

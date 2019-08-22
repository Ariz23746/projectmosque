from django.db import models

from django.db import models
from datetime import datetime


class mosquecards(models.Model):

	image = models.ImageField(upload_to='images/',blank=True)
	image2 = models.ImageField(upload_to='images/',default='',blank=True)
	image3 = models.ImageField(upload_to='images/',default='',blank=True)
	image4 = models.ImageField(upload_to='images/',default='',blank=True)
	MosqueName = models.CharField(max_length=200, default='',)
	address = models.CharField(max_length=200, default='')
	mosqueBanner = models.ImageField(upload_to='images/',default='',blank=True)
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
		

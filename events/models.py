from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.

class Event(models.Model):
	def __str__(self):
		return "Event: {} - {} ".format(self.eventName, self.date)
	eventName = models.CharField("Event Name", max_length=100, blank=False)
	date = models.DateTimeField("Date")
	description = models.TextField()
	place = models.CharField("Location", max_length=255, blank=False)
	coordinates = PlainLocationField(based_fields=['place'], zoom=7)



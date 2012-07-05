from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	name = models.CharField(max_length=100)
	time_created = models.DateTimeField('Event datetime created')
	time_started = models.DateTimeField('Event datetime starts')
	time_end = models.DateTimeField('Event datetime ends')

	def __unicode__(self):
		return self.name

class Team(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=100)
	time_add = models.DateTimeField('Team created')

	def __unicode__(self):
		return self.name

class Member(models.Model):
	team = models.ForeignKey(Team)
	user = models.ForeignKey(User)
	tel = models.CharField(max_length=30)
	time_add = models.DateTimeField('Member added')

	def __unicode__(self):
		return "%s - %s" % (self.user.username, self.tel)
	

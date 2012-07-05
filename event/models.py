from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=100)
	time_created = models.DateTimeField('Event datetime created')
	time_started = models.DateTimeField('Event datetime starts')
	time_end = models.DateTimeField('Event datetime ends')

class Team(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=100)
	time_add = models.DateTimeField('Team created')

class Member(models.Model):
	team = models.ForeignKey(Team)
	time_add = models.DateTimeField('Member added')
	

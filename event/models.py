from django.db import models
from django.contrib.auth.models import User
import datetime

class Event(models.Model):
	name = models.CharField(max_length=100)
	time_created = models.DateTimeField('Event datetime created')
	time_started = models.DateTimeField('Event datetime starts')
	time_end = models.DateTimeField('Event datetime ends')

	def __unicode__(self):
		return self.name

	def save(self):
		self.time_created = datetime.datetime.today()
		super(Event, self).save()

class Member(models.Model):
	user = models.ForeignKey(User)
	tel = models.CharField(max_length=30)
	time_created = models.DateTimeField('Member datetime added')

	def __unicode__(self):
		return "%s - %s" % (self.user.username, self.tel)

	def save(self):
		self.time_created = datetime.datetime.today()
		super(Member, self).save()

class Team(models.Model):
	event = models.ForeignKey(Event)
	leader = models.ForeignKey(Member)
	name = models.CharField(max_length=100)
	time_created = models.DateTimeField('Team datetime created')

	def __unicode__(self):
		return self.name

	def save(self):
		self.time_created = datetime.datetime.today()
		super(Team, self).save()

class Teammate(models.Model):
	team = models.ForeignKey(Team)
	member = models.ForeignKey(Member)
	time_created = models.DateTimeField('Member datetime added')

	def save(self):
		self.time_created = datetime.datetime.today()
		super(Teammate, self).save()
	

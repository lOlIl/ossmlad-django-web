from django.db import models
from django.contrib.auth.models import User
from event.models import Team

import datetime

class Problem(models.Model):
	author = models.ForeignKey(User)
	text = models.CharField(max_length=150)	
	time_created = models.DateTimeField('Problem datetime created')

	def __unicode__(self):
		return self.text

	def save(self):
		self.time_created = datetime.datetime.today()
		super(Problem, self).save()

class Solution(models.Model):
	author = models.ForeignKey(User)
	problem = models.ForeignKey(Problem)
	text = models.CharField(max_length=150)
	time_created = models.DateTimeField('Solution datetime created')

	def __unicode__(self):
		return self.text

	def save(self):
		self.time_created = datetime.datetime.today()
		super(Solution, self).save()

class TeamProblem(models.Model):
	team = models.ForeignKey(Team)
	problem = models.ForeignKey(Problem)
	time_created = models.DateTimeField('TeamProblem datetime created')

	def __unicode__(self):
		return "%s : %s" % (self.team.name, self.problem.text)

	def save(self):
		self.time_created = datetime.datetime.today()
		super(TeamProblem, self).save()

class TeamAnswer(models.Model):
	teamprob = models.ForeignKey(TeamProblem)
	text = models.CharField(max_length=150)
	time_created = models.DateTimeField('TeamProblem datetime created')
	
	def __unicode__(self):
		return self.text

	def save(self):
		self.time_created = datetime.datetime.today()
		super(TeamProblem, self).save()

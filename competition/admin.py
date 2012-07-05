from django.contrib import admin
from competition.models import Problem, Solution, TeamProblem, TeamAnswer

class ProblemAdmin(admin.ModelAdmin):
	fields = ['author', 'text']

class SolutionAdmin(admin.ModelAdmin):
	fields = ['author', 'problem', 'text']

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(TeamProblem)
admin.site.register(TeamAnswer)

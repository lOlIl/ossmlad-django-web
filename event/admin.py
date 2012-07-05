from django.contrib import admin
from event.models import Event, Team, Member

class EventAdmin(admin.ModelAdmin):
	fields = ['name', 'time_created', 'time_started', 'time_end']

admin.site.register(Event, EventAdmin)
admin.site.register(Team)
admin.site.register(Member)

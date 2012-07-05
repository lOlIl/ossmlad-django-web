from django.contrib import admin
from event.models import *

class EventAdmin(admin.ModelAdmin):
	fields = ['name', 'time_started', 'time_end']

admin.site.register(Event, EventAdmin)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Teammate)


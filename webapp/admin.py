from django.contrib import admin
from .models import User, Inter_participant, Intra_participant, Event, Council, Registration, TeamRegistration, Score

# Register your models here.

admin.site.register(User)
admin.site.register(Inter_participant)
admin.site.register(Intra_participant)
admin.site.register(Event)
admin.site.register(Council)
admin.site.register(Registration)
admin.site.register(Score)
admin.site.register(TeamRegistration)
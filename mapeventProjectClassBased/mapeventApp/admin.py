from django.contrib import admin
from mapeventApp.models import  Event, UserRegistration,AddEvent,Staff,Add

from mapeventApp.models import ChangePassword
# Register your models here.
admin.site.register(UserRegistration)
admin.site.register(Event)
admin.site.register(AddEvent)
admin.site.register(Staff)
admin.site.register(Add)


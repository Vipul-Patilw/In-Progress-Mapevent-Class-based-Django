from django.contrib import admin
from mapeventApp.models import  Event, Login,AddEvent
from mapeventApp.models import Sign
from mapeventApp.models import ChangePassword
# Register your models here.
admin.site.register(Login)
admin.site.register(Event)
admin.site.register(AddEvent)


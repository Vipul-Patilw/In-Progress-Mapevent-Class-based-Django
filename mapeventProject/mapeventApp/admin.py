from django.contrib import admin
from mapeventApp.models import  Event, Login
from mapeventApp.models import Sign
from mapeventApp.models import ChangePassword
# Register your models here.
admin.site.register(Login)
admin.site.register(Sign)
admin.site.register(ChangePassword)
admin.site.register(Event)


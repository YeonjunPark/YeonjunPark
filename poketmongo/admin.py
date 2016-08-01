from django.contrib import admin
from poketmongo.models import User
from poketmongo.models import Poketmon
from poketmongo.models import Capture
from blog.models import Zipcode


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'sex',]

admin.site.register(User, UserAdmin)

class PoketmonAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'level',]

admin.site.register(Poketmon, PoketmonAdmin)

class CaptureAdmin(admin.ModelAdmin):
    list_display = ['user', 'poketmon', 'location']

admin.site.register(Capture, CaptureAdmin)
admin.site.register(Zipcode)

from django.contrib import admin
from poketmongo.models import User
from poketmongo.models import Poketmon

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'sex',]

admin.site.register(User, UserAdmin)

class PoketmonAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'level', 'location']

admin.site.register(Poketmon, PoketmonAdmin)

from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)                   #id of every user will be displayed in read-only format.

admin.site.register(Profile,ProfileAdmin)

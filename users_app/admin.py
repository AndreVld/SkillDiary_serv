from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users_app.models import Person

admin.site.register(Person,UserAdmin)
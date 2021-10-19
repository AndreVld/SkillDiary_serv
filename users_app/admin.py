from django.contrib import admin

# Register your models here.
from users_app.models import Person, City

admin.site.register(Person)
admin.site.register(City)
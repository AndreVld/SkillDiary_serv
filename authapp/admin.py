from django.contrib import admin

from authapp.models import Person, City


class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)
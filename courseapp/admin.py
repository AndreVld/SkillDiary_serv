from django.contrib import admin
from courseapp.views import Course

from courseapp.models import Course, Profession, AdditionalInfo
admin.site.register(Course)
admin.site.register(Profession)
admin.site.register(AdditionalInfo)


from django.contrib import admin
from django.contrib.admin import site as admin_site

from authapp.models import Person
from mainapp.models import *

admin_site.site_header = 'Skilldiary Administration'
admin_site.site_title = 'Skilldiary'


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)


class ProfessionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profession, ProfessionAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)


class FileAdmin(admin.ModelAdmin):
    pass


admin.site.register(File, FileAdmin)


class HeroTextAdmin(admin.ModelAdmin):
    pass


admin.site.register(HeroText, HeroTextAdmin)


class HeroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hero, HeroAdmin)
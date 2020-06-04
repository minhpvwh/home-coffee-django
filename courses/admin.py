from django.contrib import admin
from courses.models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'num_lesson')
    search_fields = ('name',)

admin.site.register(Course, CourseAdmin)
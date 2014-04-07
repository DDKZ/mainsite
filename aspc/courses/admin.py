from django.contrib import admin
from aspc.courses.models import (Section, Course, Department, Meeting,
    RequirementArea)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'course_count')

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('section', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'begin', 'end', 'location',)

class MeetingInline(admin.TabularInline):
    model = Meeting
    list_display = ('section', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'begin', 'end', 'location',)

class CourseAdmin(admin.ModelAdmin):
    # list_display = ('code', 'name', 'instructor', 'description', 'credit', 'filled', 'spots')
    # list_filter = ('primary_department',)
    inlines = [MeetingInline,]

admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(RequirementArea, DepartmentAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Section)
from django.contrib import admin

from main.models import Student, Subject


# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('firstname', 'lastname',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'description',)
    list_filter = ('student',)
    search_fields = ('title',)

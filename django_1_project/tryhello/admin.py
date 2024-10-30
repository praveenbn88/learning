from django.contrib import admin

from tryhello.models import Student

from tryhello.models import Course

# Register your models here.


admin.site.register(Course)




class StudentAdmin(admin.ModelAdmin):
    list_filter = ('age',)
    list_display = ('name','age')
    list_editable = ('age',)
    search_fields = ('name','age')


admin.site.register(Student, StudentAdmin)



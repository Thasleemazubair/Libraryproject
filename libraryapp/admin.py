from django.contrib import admin

# Register your models here.
from .models import StudentExtra
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra,StudentExtraAdmin)
from django.contrib import admin
from course_app import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Module)
admin.site.register(models.Lesson)

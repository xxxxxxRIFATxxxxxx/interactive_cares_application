from django.contrib import admin
from auth_app import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Student)
admin.site.register(models.Instructor)
admin.site.register(models.Pending_Instructor)
admin.site.register(models.Admin)
admin.site.register(models.CSAgent)


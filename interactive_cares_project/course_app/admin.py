from django.contrib import admin
from course_app import models

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["id", "date_and_time", "student", "course", "enrollment_status"]

    class Meta:
	    model = models.Enrollment

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Module)
admin.site.register(models.Lesson)
admin.site.register(models.Quiz)
admin.site.register(models.Question)
admin.site.register(models.Enrollment, EnrollmentAdmin)
admin.site.register(models.Certificate)


from django.db import models
from auth_app.models import Instructor

# To keep each course thumbnail in a different folder
def thumbnail_upload(instance, filename):
    return f"course_app/course_thumbnails/{instance.title}/{filename}"

# Create your models here. 

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title

class Course(models.Model):
    # Instructor info
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    # Course info
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=thumbnail_upload)
    intro_video_url = models.CharField(max_length=99999)
    support_group_link = models.CharField(max_length=99999, blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    material_files_link = models.CharField(max_length=99999, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)

    difficulty_level_choices = (
        ('All Levels', 'All Levels'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    difficulty_level = models.CharField(max_length=255, choices=difficulty_level_choices, default="All Levels")
    
    course_type_choices = (
        ('Paid', 'Paid'),
        ('Free', 'Free'),
    )

    course_type = models.CharField(max_length=255, choices=course_type_choices, default="Paid")

    total_course_duration = models.CharField(max_length=255, default="00:00:00")
    price = models.FloatField(blank=True, null=True)
    discounted_price = models.FloatField(blank=True, null=True)

    # Additional info
    what_will_i_learn = models.TextField(blank=True, null=True)
    target_audience = models.TextField(blank=True, null=True)
    material_includes = models.TextField(blank=True, null=True)
    outcome = models.CharField(max_length=255, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Module name: {self.module_name}, Course: {self.course.title}"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=255)
    video_url = models.CharField(max_length=99999)
    duration = models.CharField(max_length=255, default="00:00:00")
    privacy_type_choices = (
        ('Private', 'Private'),
        ('Public', 'Public'),
    )

    privacy_type = models.CharField(max_length=255, choices=privacy_type_choices, default="Private")
    
    def __str__(self):
        return f"Lesson name: {self.lesson_name}, Module: {self.module.module_name}, Course: {self.course.title}"


   
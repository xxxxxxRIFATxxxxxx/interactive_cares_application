from django.db import models

# To create custom user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# To keep each user's profile picture in a different folder
def profile_pic_upload(instance, filename):
    return f"auth_app/profile_pics/{instance.user}/{filename}"

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, full_name, phone_number, bio, profile_picture, password):
        if not email:
            raise ValueError("User must have email!")

        if not username:
            raise ValueError("User must have username!")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, full_name=full_name, phone_number=phone_number, bio=bio, profile_picture=profile_picture)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, full_name, phone_number, bio, profile_picture, password):
        user = self.create_user(email, username, full_name, phone_number, bio, profile_picture, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=profile_pic_upload, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name", "phone_number", "bio", "profile_picture"]

    def __str__(self):
        return self.email

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")

    def __str__(self):
        return self.user.email

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="instructor_profile")

    def __str__(self):
        return self.user.email

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")

    def __str__(self):
        return self.user.email


class CSAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="csagent_profile")

    def __str__(self):
        return self.user.email







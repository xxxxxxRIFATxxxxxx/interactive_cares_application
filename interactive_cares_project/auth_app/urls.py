from django.urls import path
from auth_app import views

app_name = "auth_app"

urlpatterns = [
    path("student_signup/", views.student_signup, name="student_signup"),
    path("instructor_signup/", views.instructor_signup, name="instructor_signup"),
    path("admin_signup/", views.admin_signup, name="admin_signup"),
    path("csagent_signup/", views.csagent_signup, name="csagent_signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("password/", views.password_change, name="password_change"),
]

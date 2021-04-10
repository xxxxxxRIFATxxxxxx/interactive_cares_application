from django.urls import path
from course_app import views

app_name = "course_app"

urlpatterns = [
    # Home page URL
    path("", views.home, name="home"),

    # Course related URL
    path("courses/", views.courses, name="courses"),
    path("course_details/<pk>/", views.course_details, name="course_details"),
    path("create_course/", views.create_course, name="create_course"),
    path("edit_course/<pk>/", views.edit_course, name="edit_course"),
    path("my_courses/", views.my_courses, name="my_courses"),

    # Module related URL
    path("module_details/<pk>/", views.module_details, name="module_details"),
    path("create_module/<pk>/", views.create_module, name="create_module"),
    path("edit_module/<pk>/", views.edit_module, name="edit_module"),

    # Lesson related URL
    path("lesson_details/<pk>/", views.lesson_details, name="lesson_details"),
    path("create_lesson/<pk>/", views.create_lesson, name="create_lesson"),
    path("edit_lesson/<pk>/", views.edit_lesson, name="edit_lesson"),

    # Quiz related URL
    path("quiz_details/<pk>/", views.quiz_details, name="quiz_details"),
    path("create_quiz/<pk>/", views.create_quiz, name="create_quiz"),
    path("edit_quiz/<pk>/", views.edit_quiz, name="edit_quiz"),

    # For admin user
    path("create_category_for_admin/", views.create_category_for_admin, name="create_category_for_admin"),
    path("edit_category_for_admin/<pk>/", views.edit_category_for_admin, name="edit_category_for_admin"),
    path("category_list/", views.category_list, name="category_list"),
    path("create_course_for_admin/", views.create_course_for_admin, name="create_course_for_admin"),
    path("edit_course_for_admin/<pk>/", views.edit_course_for_admin, name="edit_course_for_admin"),
    path("create_module_for_admin/<pk>/", views.create_module_for_admin, name="create_module_for_admin"),
    path("edit_module_for_admin/<pk>/", views.edit_module_for_admin, name="edit_module_for_admin"),
    path("create_lesson_for_admin/<pk>/", views.create_lesson_for_admin, name="create_lesson_for_admin"),
    path("edit_lesson_for_admin/<pk>/", views.edit_lesson_for_admin, name="edit_lesson_for_admin"),
]

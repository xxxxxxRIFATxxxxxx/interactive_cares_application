# For Redirect
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Import Models
from course_app import models

# Import Forms
from course_app import forms

# For authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

# Homepage
def home(request):
    diction = {
        "title": "Home - Interactive Cares",
    }
    return render(request, "course_app/home.html", context=diction)

# All course list
def courses(request):
    courses = models.Course.objects.all()

    diction = {
        "title": "Courses - Interactive Cares",
        "courses": courses
    }
    return render(request, "course_app/courses.html", context=diction)

# Course details
def course_details(request, pk):
    current_course = models.Course.objects.get(pk=pk)
    modules = models.Module.objects.filter(course=current_course)

    diction = {
        "title": f"{current_course.title} - Interactive Cares",
        "current_course": current_course,
        "modules": modules
    }
    return render(request, "course_app/course_details.html", context=diction)
    
# Create course
@login_required
def create_course(request):
    form = forms.CreateCourseForm()
    created = False

    if request.method == "POST":
        form = forms.CreateCourseForm(request.POST, request.FILES)

        if form.is_valid():
            course_obj = form.save(commit=False) 
            course_obj.instructor = request.user.instructor_profile
            course_obj.save()
            created = True

    diction = {
        "title": "Create Course - Interactive Cares",
        "form": form,
        "created": created
    }
    return render(request, "course_app/create_course.html", context=diction) 

# Edit course
@login_required
def edit_course(request, pk):
    current_course = models.Course.objects.get(pk=pk)
    form = forms.CreateCourseForm(instance=current_course)

    if request.method == "POST":
        form = forms.CreateCourseForm(request.POST, request.FILES, instance=current_course)

        if form.is_valid():
            course_obj = form.save(commit=False) 
            course_obj.instructor = request.user.instructor_profile
            course_obj.save()
            return HttpResponseRedirect(reverse("course_app:course_details", kwargs={"pk":pk}))

    diction = {
        "title": "Edit Course - Interactive Cares",
        "form": form,
    }
    return render(request, "course_app/edit_course.html", context=diction) 

# My course
@login_required
def my_courses(request):
    courses = models.Course.objects.filter(instructor=request.user.instructor_profile)
    diction = {
        "title": "My Course - Interactive Cares",
        "courses": courses
    }
    return render(request, "course_app/my_courses.html", context=diction)            

# Module details
def module_details(request, pk):
    current_module = models.Module.objects.get(pk=pk)
    lessons = models.Lesson.objects.filter(module=current_module)
    quizes = models.Quiz.objects.filter(module=current_module)

    diction = {
        "title": f"{current_module.module_name} - Interactive Cares",
        "current_module": current_module,
        "lessons": lessons,
        "current_module": current_module,
        "quizes": quizes
    }
    return render(request, "course_app/module_details.html", context=diction)

# Create Module
@login_required
def create_module(request, pk):
    current_course = models.Course.objects.get(pk=pk)
    form = forms.CreateModuleForm()

    if request.method == "POST":
        form = forms.CreateModuleForm(request.POST)

        if form.is_valid():
            module_obj = form.save(commit=False) 
            module_obj.course = current_course
            module_obj.save()
            return HttpResponseRedirect(reverse("course_app:course_details", kwargs={"pk":pk}))

    diction = {
        "title": "Create Module - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/create_module.html", context=diction)

# Edit Module
@login_required
def edit_module(request, pk):
    current_module = models.Module.objects.get(pk=pk)
    form = forms.CreateModuleForm(instance=current_module)

    if request.method == "POST":
        form = forms.CreateModuleForm(request.POST, instance=current_module)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:module_details", kwargs={"pk":pk}))

    diction = {
        "title": "Edit Module - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/edit_module.html", context=diction)


# Lesson details
def lesson_details(request, pk):
    lesson = models.Lesson.objects.get(pk=pk)

    diction = {
        "title": f"{lesson.lesson_name} - Interactive Cares",
        "lesson": lesson
    }
    return render(request, "course_app/lesson_details.html", context=diction)

# Create Lesson
@login_required
def create_lesson(request, pk):
    current_module = models.Module.objects.get(pk=pk)
    form = forms.CreateLessonForm()

    if request.method == "POST":
        form = forms.CreateLessonForm(request.POST)

        if form.is_valid():
            lesson_obj = form.save(commit=False) 
            lesson_obj.course = current_module.course
            lesson_obj.module = current_module
            lesson_obj.save()
            return HttpResponseRedirect(reverse("course_app:module_details", kwargs={"pk":pk}))


    diction = {
        "title": "Create Lesson - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/create_lesson.html", context=diction)

# Edit Lesson
def edit_lesson(request, pk):
    current_lesson = models.Lesson.objects.get(pk=pk)
    form = forms.CreateLessonForm(instance=current_lesson)

    if request.method == "POST":
        form = forms.CreateLessonForm(request.POST, instance=current_lesson)

        if form.is_valid():
            lesson_obj = form.save(commit=False) 
            lesson_obj.course = current_lesson.course
            lesson_obj.module = current_lesson.module
            lesson_obj.save()
            return HttpResponseRedirect(reverse("course_app:lesson_details", kwargs={"pk":pk}))


    diction = {
        "title": "Edit Lesson - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/edit_lesson.html", context=diction)

# Quiz details
def quiz_details(request, pk):
    current_quiz = models.Quiz.objects.get(pk=pk)
    questions = models.Question.objects.filter(quiz=current_quiz)

    diction = {
        "title": f"{current_quiz.quiz_name} - Interactive Cares",
        "questions": questions
    }
    return render(request, "course_app/quiz_details.html", context=diction)


# For Admin User View

# Admin User Create Category
@login_required
def create_category_for_admin(request):
    form = forms.CreateCategoryFormForAdmin()
    created = False

    if request.method == "POST":
        form = forms.CreateCategoryFormForAdmin(request.POST)

        if form.is_valid():
            form.save()
            created = True

    diction = {
        "title": "Create Category - Interactive Cares",
        "form": form,
        "created": created
    }
    return render(request, "course_app/create_category.html", context=diction) 

# Admin User Edit Category
@login_required
def edit_category_for_admin(request, pk):
    current_category = models.Category.objects.get(pk=pk)
    form = forms.CreateCategoryFormForAdmin(instance=current_category)

    if request.method == "POST":
        form = forms.CreateCategoryFormForAdmin(request.POST, instance=current_category)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:category_list"))
            
    diction = {
        "title": "Edit Category - Interactive Cares",
        "form": form,
    }
    return render(request, "course_app/edit_category.html", context=diction) 

# Admin User Category List
@login_required
def category_list(request):
    category_list = models.Category.objects.all()
            
    diction = {
        "title": "Category List - Interactive Cares",
        "category_list": category_list
    }
    return render(request, "course_app/category_list.html", context=diction) 


# Admin User Create Course
@login_required
def create_course_for_admin(request):
    form = forms.CreateCourseFormForAdmin()
    created = False

    if request.method == "POST":
        form = forms.CreateCourseFormForAdmin(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            created = True

    diction = {
        "title": "Create Course - Interactive Cares",
        "form": form,
        "created": created
    }
    return render(request, "course_app/create_course.html", context=diction) 

# Admin User Edit Course
@login_required
def edit_course_for_admin(request, pk):
    current_course = models.Course.objects.get(pk=pk)
    form = forms.CreateCourseFormForAdmin(instance=current_course)

    if request.method == "POST":
        form = forms.CreateCourseFormForAdmin(request.POST, request.FILES, instance=current_course)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:course_details", kwargs={"pk":pk}))

    diction = {
        "title": "Edit Course - Interactive Cares",
        "form": form,
    }
    return render(request, "course_app/edit_course.html", context=diction) 

# Admin User Create Module
@login_required
def create_module_for_admin(request, pk):
    current_course = models.Course.objects.get(pk=pk)
    form = forms.CreateModuleFormForAdmin()

    if request.method == "POST":
        form = forms.CreateModuleFormForAdmin(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:course_details", kwargs={"pk":pk}))

    diction = {
        "title": "Create Module - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/create_module.html", context=diction)

# Admin User Edit Module
@login_required
def edit_module_for_admin(request, pk):
    current_module = models.Module.objects.get(pk=pk)
    form = forms.CreateModuleFormForAdmin(instance=current_module)

    if request.method == "POST":
        form = forms.CreateModuleFormForAdmin(request.POST, instance=current_module)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:module_details", kwargs={"pk":pk}))

    diction = {
        "title": "Edit Module - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/edit_module.html", context=diction)

# Admin User Create Lesson
@login_required
def create_lesson_for_admin(request, pk):
    current_module = models.Module.objects.get(pk=pk)
    form = forms.CreateLessonFormForAdmin()

    if request.method == "POST":
        form = forms.CreateLessonFormForAdmin(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:module_details", kwargs={"pk":pk}))


    diction = {
        "title": "Create Lesson - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/create_lesson.html", context=diction)

# Admin User Edit Lesson 
def edit_lesson_for_admin(request, pk):
    current_lesson = models.Lesson.objects.get(pk=pk)
    form = forms.CreateLessonFormForAdmin(instance=current_lesson)

    if request.method == "POST":
        form = forms.CreateLessonFormForAdmin(request.POST, instance=current_lesson)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_app:lesson_details", kwargs={"pk":pk}))


    diction = {
        "title": "Edit Lesson - Interactive Cares",
        "form": form
    }
    return render(request, "course_app/edit_lesson.html", context=diction)
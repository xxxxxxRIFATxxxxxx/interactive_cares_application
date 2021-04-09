# Import Forms
from auth_app import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Import Models
from auth_app import models

# For Redirect
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# For authenticate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# Student signup
def student_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("course_app:home"))
    else:
        form = forms.SignupForm()
        registered = False
    
        if request.method == 'POST':
            form = forms.SignupForm(data=request.POST)

            if form.is_valid():
                user = form.save()
                student_profile = models.Student(user=user)
                student_profile.save()
                registered = True
    
        diction = {
            "title": "Student Sign Up - Interactive Cares",
            "form": form,
            "registered": registered
        }
        return render(request, 'auth_app/signup.html', context=diction)

# Instructor signup
def pending_instructor_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("course_app:home"))
    else:   
        form = forms.SignupForm()
        registered = False
    
        if request.method == 'POST':
            form = forms.SignupForm(data=request.POST)

            if form.is_valid():
                user = form.save()
                instructor_profile = models.Pending_Instructor(user=user)
                instructor_profile.save()
                return HttpResponseRedirect(reverse("auth_app:login"))
    
        diction = {
            "title": "Instructor Sign Up - Interactive Cares",
            "form": form,
            "registered": registered
        }
        return render(request, 'auth_app/signup.html', context=diction)

# Admin signup
def admin_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("course_app:home"))
    else:
        form = forms.SignupForm()
        registered = False
        
        if request.method == 'POST':
            form = forms.SignupForm(data=request.POST)

            if form.is_valid():
                user = form.save()
                admin_profile = models.Admin(user=user)
                admin_profile.save()
                return HttpResponseRedirect(reverse("auth_app:login"))
        
        diction = {
            "title": "Admin Sign Up - Interactive Cares",
            "form": form,
            "registered": registered
        }
        return render(request, 'auth_app/signup.html', context=diction)

# CSAgent signup
def csagent_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("course_app:home"))
    else:
        form = forms.SignupForm()
        registered = False
        
        if request.method == 'POST':
            form = forms.SignupForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                csagent_profile = models.CSAgent(user=user)
                csagent_profile.save()
                return HttpResponseRedirect(reverse("auth_app:login"))
        
        diction = {
            "title": "CS Agent Sign Up - Interactive Cares",
            "form": form,
            "registered": registered
        }
        return render(request, 'auth_app/signup.html', context=diction)

# Login
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("course_app:home"))
    else:
        form = AuthenticationForm()

        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse("course_app:home"))

        diction = {
            "title": "Login - Interactive Cares",
            "form": form
        }
        return render(request, "auth_app/login.html", context=diction)

# Logout
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auth_app:login"))

# Profile view
@login_required
def profile(request):
    diction = {
        "title": "Profile - Interactive Cares",
    }
    return render(request, "auth_app/profile.html", context=diction)

# Edit profile view
@login_required
def edit_profile(request):
    form = forms.EditProfileForm(instance=request.user)

    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()

    diction = {
        "title": "Edit Profile - Interactive Cares",
        "form": form
    }
    return render(request, "auth_app/edit_profile.html", context=diction)

# Password change view
@login_required
def password_change(request):
    form = PasswordChangeForm(request.user)
    password_changed = False

    if request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)

        if form.is_valid():
            form.save()
            password_changed = True

    diction = {
        "title": "Change Password - Interactive Cares",
        "form": form,
        "password_changed": password_changed,
    }
    return render(request, "auth_app/password_change.html", context=diction)
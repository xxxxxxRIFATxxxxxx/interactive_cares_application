from django import forms
from course_app import models

# Create your forms here.

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        exclude = ("instructor",)

class CreateModuleForm(forms.ModelForm):
    class Meta:
        model = models.Module
        exclude = ("course",)

class CreateLessonForm(forms.ModelForm):
    class Meta:
        model = models.Lesson
        exclude = ("course", "module")

class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        exclude = ("course", "module")

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        exclude = ("course", "module", "quiz")


# For Admin User
class CreateCategoryFormForAdmin(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"

class CreateCourseFormForAdmin(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"

class CreateModuleFormForAdmin(forms.ModelForm):
    class Meta:
        model = models.Module
        fields = "__all__"

class CreateLessonFormForAdmin(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields = "__all__"

class CreateQuizFormForAdmin(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = "__all__"

class CreateQuestionFormForAdmin(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = "__all__"


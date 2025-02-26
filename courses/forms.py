from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from .models import Category, Course


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Category.objects.filter(parent=None)


# Custom function to validate file size
def validate_video_size(value):
    max_size = 50 * 1024 * 1024  # 50MB
    if value.size > max_size:
        raise ValidationError("Video file size must be under 50MB.")

def validate_document_size(value):
    max_size = 10 * 1024 * 1024  # 10MB
    if value.size > max_size:
        raise ValidationError("Document file size must be under 10MB.")

 
class CourseForm(forms.ModelForm):
    video = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(['mp4']), validate_video_size]
    )
    document = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(['pdf']), validate_document_size]
    )

    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'category', 'video', 'document', 'mcq']
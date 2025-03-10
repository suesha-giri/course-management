from django.db import models
from django.core.validators import FileExtensionValidator

from users.models import Student


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories')

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    #contents
    video = models.FileField(
        null=True,
        blank=True,
        upload_to='videos/',
        validators=[FileExtensionValidator(['mp4'])],
    )
    document = models.FileField(
        null=True,
        blank=True,
        upload_to='documents/',
        validators=[FileExtensionValidator(['pdf'])],
    )
    mcq = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'course')
        ordering = ['-enrolled_on']

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
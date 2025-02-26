from django.urls import path
from .views import (
    CategoryCreateUpdateView,
    CategoryDeleteView,
    CourseCreateUpdateView,
    CourseDeleteView,
    EnrollmentCreateUpdateView,
    EnrollmentDeleteView,
)


urlpatterns = [
    path('create/', CourseCreateUpdateView.as_view(), name='course-create'),
    path('update/<int:pk>/', CourseCreateUpdateView.as_view(), name='course-update'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),

    path('categories/create/', CategoryCreateUpdateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryCreateUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),

    path('enrollments/create/', EnrollmentCreateUpdateView.as_view(), name='enrollment-create'),
    path('enrollments/update/<int:pk>/', EnrollmentCreateUpdateView.as_view(), name='enrollment-update'),
    path('enrollments/delete/<int:pk>/', EnrollmentDeleteView.as_view(), name='enrollment-delete'),
]
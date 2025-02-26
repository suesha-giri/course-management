from django.urls import path
from .views import admin_login, admin_logout, dashboard, StudentCreateUpdateView, StudentDeleteView


urlpatterns = [
    path('login/', admin_login, name='login'),
    path('logout/', admin_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

    path('students/create/', StudentCreateUpdateView.as_view(), name='student-create'),
    path('students/update/<int:pk>/', StudentCreateUpdateView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
]
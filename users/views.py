from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from courses.models import Category, Course, Enrollment
from .models import Student

# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def admin_logout(request):
    logout(request)
    return redirect('dashboard')


def dashboard(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        categories = Category.objects.all()
        students = Student.objects.all()
        enrollments = Enrollment.objects.all()
        context = {'courses': courses, 'categories': categories, 'students': students, 'enrollments': enrollments}
        return render(request, 'dashboard.html', context=context)
    return redirect('login')


class StudentCreateUpdateView(CreateView, UpdateView):
    model = Student
    fields = ['name', 'email']
    template_name = 'student_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        """
        If updating, return the student instance, otherwise create a new one.
        """
        if self.kwargs.get('pk'):
            return get_object_or_404(Student, pk=self.kwargs['pk'])
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['form_action'] = 'Update'
            context['form_url'] = reverse('student-update', args=[self.object.pk])
        else:
            context['form_action'] = 'Create'
            context['form_url'] = reverse('student-update', args=[self.object.pk])
        return context



class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'generic_delete_template.html'
    success_url = reverse_lazy('dashboard') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context
    
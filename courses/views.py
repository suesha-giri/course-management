from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Category, Enrollment, Course
from .forms import CategoryForm, CourseForm

# Create your views here.


class CategoryCreateUpdateView(CreateView, UpdateView):
    model = Category
    form_class = CategoryForm  # Use custom form
    template_name = 'category_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        """
        If updating, return the category instance, otherwise create a new one.
        """
        if self.kwargs.get('pk'):
            return get_object_or_404(Category, pk=self.kwargs['pk'])
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['form_action'] = 'Update'
            context['form_url'] = reverse('category-update', args=[self.object.pk])
        else:
            context['form_action'] = 'Create'
            context['form_url'] = reverse('category-create')
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'generic_delete_template.html'
    success_url = reverse_lazy('dashboard') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context
    

class CourseCreateUpdateView(CreateView, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        """
        If updating, return the course instance, otherwise create a new one.
        """
        if self.kwargs.get('pk'):
            return get_object_or_404(Course, pk=self.kwargs['pk'])
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['form_action'] = 'Update'
            context['form_url'] = reverse('course-update', args=[self.object.pk])
        else:
            context['form_action'] = 'Create'
            context['form_url'] = reverse('course-create')
        return context


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'generic_delete_template.html'
    success_url = reverse_lazy('dashboard') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context
    

class EnrollmentCreateUpdateView(CreateView, UpdateView):
    model = Enrollment
    fields= ['student', 'course', 'is_completed']
    template_name = 'enrollment_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        """
        If updating, return the enrollment instance, otherwise create a new one.
        """
        if self.kwargs.get('pk'):
            return get_object_or_404(Enrollment, pk=self.kwargs['pk'])
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['form_action'] = 'Update'
            context['form_url'] = reverse('enrollment-update', args=[self.object.pk])
        else:
            context['form_action'] = 'Create'
            context['form_url'] = reverse('enrollment-create')
        return context


class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'generic_delete_template.html'
    success_url = reverse_lazy('dashboard') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context
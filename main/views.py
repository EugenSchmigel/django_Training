from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from config import settings
from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


@login_required
def index(request):
    students_list = Student.objects.all()
    context = {
        'object_list': students_list,
    }

    return render(request, 'main/student_list.html', context)


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    # fields = ('firstname', 'lastname', 'avatar')
    form_class = StudentForm
    permission_required = 'main.add_student'
    success_url = reverse_lazy('main:index')
    extra_context = {'title': 'Create Student'}


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    extra_context = {'title': 'Student List'}


@login_required
@permission_required('main.view_student')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}: ({email}): {message}')

    context = {
        'title': 'Contact'
    }
    return render(request, 'main/contact.html', context)


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    permission_required = 'main.view_student'
    extra_context = {'title': 'Student Details'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        key = f'subject_list_{self.object.pk}'
        if settings.CACHE_ENABLED:
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list = self.object.subject_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()

        context_data['subject'] = subject_list
        return context_data



class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    # fields = ('firstname', 'lastname', 'avatar')
    form_class = StudentForm
    permission_required = 'main.change_student'
    success_url = reverse_lazy('main:index')
    extra_context = {'title': 'Update Student'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    # permission_required = 'main.delete_student'
    success_url = reverse_lazy('main:index')
    extra_context = {'title': 'Delete Student'}

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@permission_required('main.change_student')
def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:index'))


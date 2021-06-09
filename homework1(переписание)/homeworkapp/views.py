from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.edit import CreateView ,UpdateView

from homeworkapp.models import Company, Employee


class home(TemplateView):
    template_name = 'home.html'


class Show(ListView):
    model = Company

class Edit(UpdateView):
    model = Employee
    fields = ['department','first_name','last_name','job_description','age']
    def form_valid(self, form):
        return self.form_valid(form)

class delete(DeleteView):
    model = Employee


class CreateEmployee(CreateView):
    model = Employee
    fields = ['department','first_name','last_name','job_description','age']
    def form_valid(self, form):
        return self.form_valid(form)
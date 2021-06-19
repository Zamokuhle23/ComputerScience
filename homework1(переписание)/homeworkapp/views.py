from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.edit import CreateView ,UpdateView

from homeworkapp.models import Company, Employee


class home(TemplateView):
    template_name = 'home.html'


class Show(ListView):
    model = Company

class Edit(UpdateView):
    model = Company

    fields = ['department','first_name','last_name','job_description','age']

    def form_valid(self, form):
        return self.form_valid(form)

    def get_queryset(self):
        queryset = self.get_queryset()


class delete(DeleteView):
    model = Company


class CreateEmployee(CreateView):
    model = Employee
    fields = ['department','first_name','last_name','job_description','age']
    def form_valid(self, form):
        return self.form_valid(form)
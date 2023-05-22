from django.shortcuts import render
from app1.models import *
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

class home(TemplateView):
    template_name='app1\home.html'

class list_view(ListView):
    model=School
    context_object_name='school'

class detail_view(DetailView):
    model=School
    context_object_name='sclobject'

class create_view(CreateView):
    model=School
    fields='__all__'

class update_view(UpdateView):
    model=School
    fields='__all__'

class delete_view(DeleteView):
    model=School
    context_object_name='SDO'
    success_url=reverse_lazy('list_view')

from myinfo.models import Data
from django.shortcuts import render, get_object_or_404, redirect
from myinfo.forms import DataForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class AboutMe(TemplateView):
    template_name='about.html'



class CreatePostView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'myinfo/home.html'

    form_class = DataForm

    model = Data



class DataListView(ListView):
    model = Data

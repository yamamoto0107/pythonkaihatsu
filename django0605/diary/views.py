from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .forms import DiaryForm
from django.urls import reverse_lazy
from .models import Diary
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary

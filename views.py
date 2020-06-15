from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from .models import Choice,Calorie,TOP
from django.urls import reverse_lazy
from . forms import CalorieForm,TOPForm
from django.contrib.auth import authenticate, login
# Create your views here.
# class Top(TemplateView):
#     template_name = "cal/index.html"

class TOPListView(ListView):
    model=TOP
    template_name='cal/cal_list.html'

class CalorieListView(ListView):
    model=Calorie
    template_name='cal/item_list.html'

class DayCreateView(CreateView):
    model=TOP
    form_class=TOPForm
    success_url = reverse_lazy('cal:create_done')

class CalorieCreateView(CreateView):
    model=Calorie
    form_class=CalorieForm
    success_url = reverse_lazy('cal:create_done')


class TOPUpdateView(UpdateView):
    model=TOP
    form_class=TOPForm
    success_url=reverse_lazy('cal:update_done')

def update_done(request):
    return render(request, 'cal/update_done.html')

def create_done(request):
    return render(request,'cal/create_done.html')

class TOPDeleteView(DeleteView):
    model=TOP
    success_url = reverse_lazy('cal:delete_done')

def delete_done(request):
    return render(request, 'cal/delete_done.html')

def loginfunc(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return render(request,'cal/cal_list.html')
        else:
           return render(request,'cal/index.html',{'error':'IDまたはpasswordが正しくありません。'})
    return render(request,'cal/index.html')
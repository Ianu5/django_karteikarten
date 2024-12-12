from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Card, Tag
from .forms import CardForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'vocabulary/home.html'


class UserLogin(LoginView):
    template_name = 'vocabulary/registration/login.html'
    success_url = reverse_lazy('home')


class UserRegistration(CreateView):
    template_name = 'vocabulary/registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CreateCard(CreateView):
    model = Card
    template_name = 'vocabulary/add_card.html'
    form_class = CardForm
    success_url = reverse_lazy('add_card')

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'vocabulary/card_list.html'
    context_object_name = 'cards'

def logoutuser(request):
    logout(request)
    return redirect('/')
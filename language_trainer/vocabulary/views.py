from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Card, Tag
from .forms import CardForm, TagForm

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


def logoutuser(request):
    logout(request)
    return redirect('/')


class CreateCard(CreateView):
    model = Card
    template_name = 'vocabulary/add_card.html'
    form_class = CardForm
    success_url = reverse_lazy('add_card')


class CardUpdate(UpdateView):
    model = Card
    template_name = 'vocabulary/card_edit.html'
    form_class = CardForm
    success_url = reverse_lazy('card_list')


class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'vocabulary/card_list.html'
    context_object_name = 'cards'


def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect('card_list')
    

class CreateTag(CreateView):
    model = Tag
    template_name = 'vocabulary/add_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('add_card')


class TagListView(ListView):
    model = Tag
    template_name = 'vocabulary/tag_list.html'
    context_object_name = 'tags'


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')
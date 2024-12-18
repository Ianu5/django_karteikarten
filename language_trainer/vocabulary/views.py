from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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


class CreateCard(LoginRequiredMixin, CreateView):
    model = Card
    template_name = 'vocabulary/add_card.html'
    form_class = CardForm
    success_url = reverse_lazy('add_card')


class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = 'vocabulary/card_edit.html'
    form_class = CardForm
    success_url = reverse_lazy('card_list')


class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'vocabulary/card_list.html'
    context_object_name = 'cards'


@login_required
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect('card_list')
    

class CreateTag(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'vocabulary/add_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('add_card')


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'vocabulary/tag_list.html'
    context_object_name = 'tags'


@login_required
def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')


# I need to rewrite this class maybe even make a function out of it to make it easier
# When writing a function I might need 2 templates one for choosing the tag and one for rendering the list with the cards
class CardFilteredListView(ListView):
    model = Card
    template_name = 'filtered_cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        queryset = Card.objects.all()
        tag_name = self.request.GET.get('tag', None)

        if tag_name:
            queryset = queryset.filter(tags__name=tag_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
from django.urls import path
from .views import UserLogin, UserRegistration, HomeView, CardListView, logoutuser, CreateCard, delete_card, CardUpdate, CreateTag, CardFilteredListView
from .views import TagListView, delete_tag
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', UserLogin.as_view(next_page="/"), name='login'),
    path('register', UserRegistration.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('card/list', CardListView.as_view(), name='card_list'),
    path('logout', logoutuser, name='logout'),
    path('add_card', CreateCard.as_view(), name='add_card'),
    path('cards/<int:pk>/delete', delete_card, name='delete_card'),
    path('cards/<int:pk>/edit/', CardUpdate.as_view(), name='edit_card'),
    path('tag/add', CreateTag.as_view(), name='add_tag'),
    path('tag/<int:pk>/delete', delete_tag, name='delete_tag'),
    path('tag/list', TagListView.as_view(), name='tag_list'),
    path('card/filtered/', CardFilteredListView.as_view(), name="filtered_cards"),
]
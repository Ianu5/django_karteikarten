from django.urls import path
from .views import UserLogin, UserRegistration, HomeView, CardListView, logoutuser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', UserLogin.as_view(next_page="/"), name='login'),
    path('register', UserRegistration.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('cards', CardListView.as_view(), name='card_list'),
    path('logout', logoutuser, name='logout'),
]
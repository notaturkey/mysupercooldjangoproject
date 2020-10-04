from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/',views.index, name='index'),
    path('user/<str:userName>/', views.user, name="user"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]
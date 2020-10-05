from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/',views.index, name='index'),
    path('user/<str:userName>/', views.user, name="user"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', views.account, name='account'),
    path('thanks/' , views.thanks, name='thanks'),
    path('signup/', views.signup, name='signup'),
    path('search/<str:userName>/', views.search, name='search')
    
]

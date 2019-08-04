    
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='login'),
    path('logout', views.logout, name='signout'),
]
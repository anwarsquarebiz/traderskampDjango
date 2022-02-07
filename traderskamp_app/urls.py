from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signin', views.signIn, name='signin'),
    path('signout', views.signOut, name='signout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
]

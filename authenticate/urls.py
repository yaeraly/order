from django.urls import path
from . import views

app_name = 'authenticate'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('send/', views.send, name='send'),
    path('receive/', views.receive, name='receive'),
    path('signin/', views.signin, name='signin'),
]

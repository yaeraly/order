from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
]

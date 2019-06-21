from django.urls import path
from .views import *
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('create/', views.ListCreate.as_view()),
    path('<int:pk>/delete/', views.ListDelete.as_view()),

]

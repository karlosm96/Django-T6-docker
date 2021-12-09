from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.details, name='details'),
    path('<int:poll_id>/results/', views.results, name='results'),
]
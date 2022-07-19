from django.urls import path
from . import views

app_name = 'starships'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.CreateStarshipView.as_view(), name='create-starship'),
    path('<int:pk>/', views.StarshipDetailView.as_view(), name='view-starship'),
    path('<int:pk>/edit/', views.UpdateStarshipView.as_view(), name='update-starship'),
    path('<int:pk>/delete/', views.DeleteStarshipView.as_view(), name='delete-starship')
]
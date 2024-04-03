from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name="portfolio-index"),
    path('<int:proj_id>/', views.detale_project, name='project_detale'),
]
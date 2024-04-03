from django.urls import path
from blog import views
urlpatterns = [
    path('', views.blog, name="blog-blog"),
    path('<int:Blog_id>/', views.detaele_blog, name='blog_detale'),
]
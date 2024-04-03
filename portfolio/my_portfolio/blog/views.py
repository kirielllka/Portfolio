from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.template.response import TemplateResponse
from blog.models import Blog
# Create your views here.
def blog(request: HttpRequest) -> TemplateResponse:
    projects = Blog.objects.all()
    return render(request=request, template_name="blog/blog.html",context={'projects':projects})

def detaele_blog(request: HttpRequest, Blog_id:int) -> TemplateResponse:
    blog = get_object_or_404(Blog, pk=Blog_id)
    return render(request, 'blog/detaele_blog.html', {'blog': blog})
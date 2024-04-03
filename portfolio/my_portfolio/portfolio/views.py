from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.template.response import TemplateResponse
from portfolio.models import Project
from blog.models import Blog
# Create your views here.
def index(request: HttpRequest) -> TemplateResponse:
    projects = Project.objects.all()
    return render(request=request, template_name="portfolio/index.html",context={'projects':projects})

def detale_project(request: HttpRequest, proj_id:int) -> TemplateResponse:
    project = get_object_or_404(Project, pk= proj_id)
    return render(request, 'portfolio/project.html', {'project': project})


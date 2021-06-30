from django.shortcuts import render
from .models import Aboutpage, Projects

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, "portfolio/home.html", {"projects": projects})


def about(request):
    propic = Aboutpage.objects.all()
    return render(request, "portfolio/about.html", {"propic": propic})


def blog(request):
    return render(request, "portfolio/blog.html")

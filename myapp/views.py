from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
def about(request):
    return render(request, 'myapp/about.html')
def skill(request):
    return render(request, 'myapp/skill.html')
def project(request):
    return render(request, 'myapp/project.html')
def contect(request):
    return render(request, 'myapp/contect.html')
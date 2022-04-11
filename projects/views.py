from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import context
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm

# Create your views here.

def index(request):

    projects = Project.objects.all()

    context= {
        'projects': projects,
    }
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    
    project = get_object_or_404(Project, id= pk)
    context= {
        'project': project,
    }
    return render(request, 'projects/project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project created Successfully!')
            return redirect('projects')

    context = {
        'form':form
    }

    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            messages.success(request, 'Project Updated!')
            return redirect('account')

    context = {
        'form':form
    }

    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, 'Project Deleted!')
        return redirect('account')

    context = {
        'object': project
    }
    return render(request, 'delete_template.html', context)
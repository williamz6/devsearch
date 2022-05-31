from posixpath import split
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import context
from django.contrib import messages
from django.core import paginator
from .models import Project, Tag
from .utils import searchProject, paginateProject
from .forms import ProjectForm, ReviewForm
import re


# Create your views here.
# projects view
def index(request):
    projects, search_query = searchProject(request)
    
    custom_range, projects = paginateProject(request, projects)
   

    context= {
        'projects': projects,
        'search_query': search_query,
        'custom_range':custom_range,
    }
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    
    project = get_object_or_404(Project, id= pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        project.getVoteCount

        messages.success(request, 'Review added')
        return redirect('project', pk=project.id)
    context= {
        'project': project,
        'form': form
    }
    return render(request, 'projects/project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created= Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
                
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
        
        newtags = request.POST.get('newtags').replace(',', " ").split()
       
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created= Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            messages.success(request, 'Project Updated!')
            return redirect('account')

    context = {
        'form':form,
        'project':project,
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


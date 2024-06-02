from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Directory, Document
from .forms import DirectoryForm, DocumentForm, ConnexionForm


# Create your views here.


def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('directory_list')  # redirige vers la liste des répertoires après connexion
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
            return render(request, 'ged/login.html')
    else:
        return render(request, 'ged/login.html')

@login_required
def directory_list(request):
    directories = Directory.objects.filter(parent=None)
    return render(request, 'ged/list.html', {'directories': directories})

@login_required
def directory_detail(request, pk):
    directory = get_object_or_404(Directory, pk=pk)
    subdirectories = directory.subdirectories.all()
    documents = Document.objects.filter(directory=directory)
    return render(request, 'ged/detail.html', {
        'directory': directory,
        'subdirectories': subdirectories,
        'documents': documents,
    })

@login_required
def add_directory(request):
    if request.method == 'POST':
        form = DirectoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directory_list')
    else:
        form = DirectoryForm()
    return render(request, 'ged/directory.html', {'form': form})

@login_required
def add_subdirectory(request, pk):
    parent_directory = get_object_or_404(Directory, pk=pk)
    if request.method == 'POST':
        form = DirectoryForm(request.POST)
        if form.is_valid():
            subdirectory = form.save(commit=False)
            subdirectory.parent = parent_directory
            subdirectory.save()
            return redirect('directory_detail', pk=parent_directory.pk)
    else:
        form = DirectoryForm()
    return render(request, 'ged/children.html', {
        'form': form,
        'parent_directory': parent_directory
    })

@login_required
def add_document(request, pk):
    directory = get_object_or_404(Directory, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.directory = directory
            document.save()
            return redirect('directory_detail', pk=directory.pk)
    else:
        form = DocumentForm()
    return render(request, 'ged/document.html', {'form': form, 'directory': directory})
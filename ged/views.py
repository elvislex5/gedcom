from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Directory, Document, ArchiveDocument
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
            directory = form.save(commit=False)
            directory.owner = request.user
            directory.save()
            return redirect('directory_list')
    else:
        form = DirectoryForm()
    return render(request, 'ged/directory.html', {'form': form})

@login_required
def add_subdirectory(request, pk):
    parent_directory = get_object_or_404(Directory, pk
    =pk)
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
def add_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            return redirect('directory_detail', pk=document.directory.pk)
    else:
        form = DocumentForm()
    return render(request, 'ged/list.html', {'form': form})

def statistics(request):
    total_directories = Directory.objects.count()
    total_documents = Document.objects.count()
    total_size = Document.objects.aggregate(total_size=models.Sum('file'))['total_size'] or 0

    context = {
        'total_directories': total_directories,
        'total_documents': total_documents,
        'total_size': total_size,
    }
    return render(request, 'ged/statistics.html', context)

@login_required()
def archive_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        archived_document = ArchiveDocument.objects.create(
            name = document.name,
            file = document.file,
            archived_by = request.user
        )
        document.delete()
        return redirect('directory_detail', pk=document.directory.pk)
    return render(request, 'ged/archive_document.html', {'document': document})

@login_required()
def archived_documents(request):
    archived_docs = ArchiveDocument.objects.all()
    return render(request, 'ged/archives.html', {'archived_docs': archived_docs})

@login_required
def delete_directory(request, pk):
    directory = get_object_or_404(Directory, pk=pk)
    if request.method == 'POST':
        parent_directory = directory.parent
        directory.delete()
        if parent_directory:
            return redirect('directory_detail', pk=parent_directory.pk)
        else:
            return redirect('directory_list')
    return render(request, 'ged/delete.html', {'object': directory, 'type': 'directory'})

@login_required
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        directory_id = document.directory.pk
        document.delete()
        return redirect('directory_detail', pk=directory_id)
    return render(request, 'ged/delete.html', {'object': document, 'type': 'document'})

@login_required
def delete_subdirectory(request, pk):
    subdirectory = get_object_or_404(Directory, pk=pk)
    if request.method == 'POST':
        parent_directory = subdirectory.parent
        subdirectory.delete()
        return redirect('directory_detail', pk=parent_directory.pk)
    return render(request, 'ged/delete.html', {'object': subdirectory, 'type': 'subdirectory'})


@login_required
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('directory_detail', pk=document.directory.pk)
    else:
        form = DocumentForm(instance=document)
    return render(request, 'ged/edit_document.html', {'form': form, 'document': document})

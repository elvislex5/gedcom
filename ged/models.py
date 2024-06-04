from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Directory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subdirectories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Document(models.Model):
    directory = models.ForeignKey(Directory, related_name='documents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(default=0)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ArchiveDocument(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='archives/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    archived_at = models.DateTimeField(auto_now_add=True)
    archived_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



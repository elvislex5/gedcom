from django.contrib import admin
from .models import Document, Directory, ArchiveDocument

# Register your models here.

admin.site.register(Directory)
admin.site.register(Document)
admin.site.register(ArchiveDocument)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('search/', views.search, name='search'),
    path('directory_list/', views.directory_list, name='directory_list'),
    path('directory/add_directory/', views.add_directory, name='add_directory'),
    path('directory/<int:pk>/delete/', views.delete_directory, name='delete_directory'),
    path('add_document/', views.add_document, name='add_document'),
    path('statistics/', views.statistics, name='statistics'),
    path('archive/', views.archived_documents, name='archived_documents'),
    path('archived/<int:pk>/delete/', views.delete_archived_document, name='delete_archived_document'),
    path('documents/archived/<int:pk>/restore/', views.restore_archived_document, name='restore_archived_document'),
    path('document/<int:pk>/archive/', views.archive_document, name='archive_document'),
    path('document/<int:pk>/delete/', views.delete_document, name='delete_document'),
    path('document/<int:pk>/edit/', views.edit_document, name='edit_document'),
    path('directory/<int:pk>/subdirectory/delete/', views.delete_subdirectory, name='delete_subdirectory'),
    path('directory/<int:pk>/', views.directory_detail, name='directory_detail'),
    # path('directory/<int:parent_id>/add_document/', views.add_document, name='add_document'),
    path('directory/<int:pk>/add_subdirectory/', views.add_subdirectory, name='add_subdirectory'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('directory_list/', views.directory_list, name='directory_list'),
    path('directory/add_directory/', views.add_directory, name='add_directory'),
    path('directory/<int:pk>/', views.directory_detail, name='directory_detail'),
    # path('directory/<int:parent_id>/add_document/', views.add_document, name='add_document'),
    path('directory/<int:pk>/add_document/', views.add_document, name='add_document'),
    path('directory/<int:pk>/add_subdirectory/', views.add_subdirectory, name='add_subdirectory'),
]
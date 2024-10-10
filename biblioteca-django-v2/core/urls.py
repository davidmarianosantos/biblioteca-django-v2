from django.urls import path
from . import views

urlpatterns = [

    #Livros
    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),

    #Autor
    path('autores/', views.AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),

    #Categoria
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
]

from rest_framework import generics
from .models import Livro, Categoria,Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from .filters import LivroFilter, CategoriaFilter

# Views dos livros
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"
    filterset_class = LivroFilter
    search_fields = ['^titulo', '^autor__nome', '^categoria__nome'] 
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

# Views das categorias
 
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    name = "categoria-list"
    search_fields = ("^nome",)
    ordering_fields = ['nome']

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

# Views dos autores
 
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = CategoriaSerializer
    name = "autor-list"
    
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

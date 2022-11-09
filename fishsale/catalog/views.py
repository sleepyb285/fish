from django.shortcuts import render
from .models import Category,Product
from django.views import generic

# Create your views here.

class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10

class ProductDetailView(generic.DetailView):
    model = Product

class CategoryListView(generic.ListView):
    model = Category

def index(request):
    random_product = Product.objects.order_by('?')[:10]
    return render(request,'index.html',{'random_product': random_product})

def catalog(request):
    return render(request, 'catalog.html')
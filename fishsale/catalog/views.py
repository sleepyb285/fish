from django.shortcuts import render
from .models import Category,Product
from django.views import generic

# Create your views here.
def index(request):
    return render(request,'index.html')
class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10
class ProductDetailView(generic.DetailView):
    model = Product

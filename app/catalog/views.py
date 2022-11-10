from django.shortcuts import render
from .models import Category, Fish
from django.views import generic

# Create your views here.
def index(request):
    return render (request,'index.html')
def catalog(request):
    categories = Category.objects.all()
    fishies = Fish.objects.all()
    return render (request,'catalog.html',{'categories':categories,'fishies':fishies})

class FishDetailView (generic.DetailView):
    model = Fish

class CategoryDetailView (generic.DetailView):
    model = Category
    paginate_by = 10
#Не забыть узнать, будет ли это работать с другими моделями в html
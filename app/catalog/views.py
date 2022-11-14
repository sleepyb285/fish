from django.shortcuts import render
from .models import Category, Fish
from django.http import Http404

# Create your views here.
def index(request):
    return render (request,'index.html')


def catalog(request):
    categories = Category.objects.all()
    fishies = Fish.objects.all()
    return render (request,'catalog.html',{'categories':categories,'fishies':fishies})

def FishDetailView (request, slug):
    try:
        fish = Fish.objects.get(slug=slug)
        cat = Category.objects.get(id = fish.category.id)
    except Fish.DoesNotExist:
        raise Http404()   
    return render (request,'fish_detail.html',{'fish':fish, 'cat':cat})

def CategoryDetailView (request,slug):
    try:
        cat = Category.objects.get(slug=slug)
        fishies = Fish.objects.filter(category = cat.id)
    except Category.DoesNotExist:
        raise Http404()
    return render (request,'category_detail.html', {'cat':cat, 'fishies':fishies})

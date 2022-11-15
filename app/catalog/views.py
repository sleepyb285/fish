from django.shortcuts import render
from .models import Category, Fish, Provider,FilterInfo, Attribute
from django.http import Http404

# Create your views here.
def index(request):
    return render (request,'index.html')


def catalog(request):
    categories = Category.objects.all()
    fishies = Fish.objects.all()
    providers = Provider.objects.all()
    return render (request,'catalog.html',{'categories':categories,'fishies':fishies, 'providers':providers})

def FishDetailView (request, slug):
    try:
        fish = Fish.objects.get(slug=slug)



    except Fish.DoesNotExist:
        raise Http404()   
    return render (request,'fish_detail.html',{'fish':fish})

def CategoryDetailView (request,slug):
    try:
        cat = Category.objects.get(slug=slug)
        fishies = Fish.objects.filter(category = cat.id)
    except Category.DoesNotExist:
        raise Http404()
    return render (request,'category_detail.html', {'cat':cat, 'fishies':fishies})

def feedback(request):
    return render(request, 'feedback.html')

def contacts(request):
    return render(request, 'contacts.html')

def ProviderDetailView(request, slug):
    try:
        prov = Provider.objects.get(slug=slug)
        fishies = Fish.objects.filter(provider = prov.id)

    except Provider.DoesNotExist:
        raise Http404()
    return render(request, 'provider_detail.html', {'provider':prov, 'fishies':fishies})



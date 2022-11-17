from django.shortcuts import render
from .models import Category, Fish, Provider,FilterInfo, Attribute, Feedback
from django.http import Http404

# Create your views here.
def index(request):
    random_fish = Fish.objects.order_by('?')[:12]
    return render (request,'index.html', {'random_fish':random_fish})


def catalog(request):
    categories = Category.objects.all()
    fishies = Fish.objects.all()
    providers = Provider.objects.all()
    return render (request,'catalog.html',{'categories':categories,'fishies':fishies, 'providers':providers})

def FishDetailView (request, slug):
    try:
        fish = Fish.objects.get(slug=slug)
        shitfan = Feedback.objects.filter(fish = fish.id)
    except Fish.DoesNotExist:
        raise Http404()   
    return render (request,'fish_detail.html',{'fish':fish, 'shitfan':shitfan})

def CategoryDetailView (request,slug):
    try:
        cat = Category.objects.get(slug=slug)
        # children = Category.objects.filter(parent = cat.id)
        fishies = Fish.objects.filter(category = cat.id or cat.children.id)
        
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



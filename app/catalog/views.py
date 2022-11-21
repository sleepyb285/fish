from django.shortcuts import render
from .models import Category, Fish, Provider, Feedback, Location, Callback_request, Feedback_generic
from django.http import Http404,HttpResponseRedirect
from .forms import CallbackForm, FeedbackForm, Feedback_newForm
from datetime import datetime

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
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            a = Feedback(
                name = form.cleaned_data["name"],
                body = form.cleaned_data["body"],
                image = form.cleaned_data["image"],
                fish = form.cleaned_data["fish"],
                date = datetime.now()
            )
            a.save()
            return HttpResponseRedirect('/nice/')
    else:
        form = FeedbackForm(initial = {'fish': Fish.objects.get(slug=slug)})
    try:
        fish = Fish.objects.get(slug=slug)
        shitfan = Feedback.objects.filter(fish = fish.id)
    except Fish.DoesNotExist:
            raise Http404()   

    return render (request,'fish_detail.html',{'fish':fish, 'shitfan':shitfan, 'form':form})

def CategoryDetailView (request,slug):
    try:
        cat = Category.objects.get(slug=slug)
        # children = Category.objects.filter(parent = cat.id)
        fishies = Fish.objects.filter(category = cat.id or cat.children.id)
        
    except Category.DoesNotExist:
        raise Http404()
    return render (request,'category_detail.html', {'cat':cat, 'fishies':fishies})

def contacts(request):
    locations = Location.objects.all()
    return render(request, 'contacts.html', {'locations':locations})

def ProviderDetailView(request, slug):
    try:
        prov = Provider.objects.get(slug=slug)
        fishies = Fish.objects.filter(provider = prov.id)

    except Provider.DoesNotExist:
        raise Http404()
    return render(request, 'provider_detail.html', {'provider':prov, 'fishies':fishies})

def LocationDetailView(request,id):

    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            a = Callback_request(
                name = form.cleaned_data["name"],
                phone = form.cleaned_data["phone"],
                email = form.cleaned_data["email"],
                text = form.cleaned_data["text"],
                # location = id
            )
            a.save()
            return HttpResponseRedirect('/nice/')
    else:
        form = CallbackForm()
    try:
        location = Location.objects.get(id = id)
    except Location.DoesNotExist:
        raise Http404()
    return render(request, 'location_detail.html', {'location':location, 'form':form})

def nice(request):
    return render(request, 'nice.html')

def feedback(request):
    shitfan = Feedback_generic.objects.all()
    return render(request, 'feedback.html', {'shitfan':shitfan})


def feedback_new(request):

    if request.method == 'POST':
        form = Feedback_newForm(request.POST)
        print(request)
        print(form.data)
        if form.is_valid():
            upload = request.FILES
            a = Feedback_generic(
                name = form.cleaned_data["name"],
                body = form.cleaned_data["body"],
                image = form.cleaned_data["image"],
                date = datetime.now()
            )

            a.save()
            
            return HttpResponseRedirect('/feedback/')

    else:
        form = Feedback_newForm()

    return render(request, 'new.html', {'form':form})


from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Fish, Provider, Feedback, Location, Callback_request, Feedback_generic, FilterInfo
from django.http import Http404,HttpResponseRedirect
from .forms import CallbackForm, FeedbackForm, Feedback_newForm
from datetime import datetime

# Create your views here.
def index(request):
    random_fish = Fish.objects.order_by('?')[:12]
    categories = Category.objects.filter(parent = None)
    return render (request,'index.html', {'categories':categories,'random_fish':random_fish})


def catalog(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            a = Callback_request(
                name = form.cleaned_data["name"],
                phone = form.cleaned_data["phone"],
                email = form.cleaned_data["email"],
                text = form.cleaned_data["text"],
            )
            a.save()
            return HttpResponseRedirect('/nice/')
    else:
        form = CallbackForm()
    categories = Category.objects.filter(parent = None)
    subcategories = Category.objects.filter(children = None)
    fishies = Fish.objects.all()
    attributes = FilterInfo.objects.all()
    paginator = Paginator(fishies, 12)
    providers = Provider.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = len(fishies)
    form = CallbackForm
    return render (request,'catalog.html',{'categories':categories,'fishies':page_obj, 'providers':providers, 'subcategories':subcategories, 'count':count, 'form':form, 'attributes':attributes})


def FishDetailView (request, slug):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        
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
        paginator = Paginator(shitfan,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Fish.DoesNotExist:
            raise Http404()   

    return render (request,'fish_detail.html',{'fish':fish, 'shitfan':page_obj, 'form':form})

def CategoryDetailView (request,slug):
    try:
        cat = Category.objects.get(slug=slug)
        children = Category.objects.filter(parent = cat.id)
        fishies = Fish.objects.filter(category = cat.id)
        for child in children:
            fishies |= Fish.objects.filter(category = child.id)
        paginator = Paginator(fishies,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Category.DoesNotExist:
        raise Http404()
    return render (request,'category_detail.html', {'cat':cat, 'fishies':page_obj, 'children':children})

def contacts(request):
    locations = Location.objects.all()
    return render(request, 'contacts.html', {'locations':locations})

def ProviderDetailView(request, slug):
    try:
        prov = Provider.objects.get(slug=slug)
        fishies = Fish.objects.filter(provider = prov.id)
        paginator = Paginator(fishies,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Provider.DoesNotExist:
        raise Http404()
    return render(request, 'provider_detail.html', {'provider':prov, 'fishies':page_obj})

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
    paginator = Paginator(shitfan,16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feedback.html', {'shitfan':page_obj})


def feedback_new(request):

    if request.method == 'POST':
        form = Feedback_newForm(request.POST,request.FILES)
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

def about(request):
    
    return render(request, 'about.html')
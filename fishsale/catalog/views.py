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
    return render(request,'index.html',{'random_product': random_product}) #Читал, что это плохо при больших размерах бд, но пока сойдет

def catalog(request):
    # category_list = Category.objects.all()
    # product_list = Product.objects.all()
    return render(request, 'catalog.html')#, {'category_list':category_list}, {'product_list':product_list})
    # сука, не работает. Получается Manager(что мне не нужно), нужно его как-то преобразовать? отдельно запрашивать типы данных и заворачивать в массив?
    # Неужели нет простого способа брать данные из двух моделей? Сделать третью, наследника первых двух?
    # Прописать в модель способ вывода данных из неё сразу? Циклами писать в массив ещё в функции модели, а потом вызывать уже это? (скорее всего)
    # а в актуальном варианте он вообще переходит на язык забытых богов
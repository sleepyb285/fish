from django.urls import path, re_path
from . import views
from .views import ProductListView, ProductDetailView, CategoryListView


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^products/$', views.ProductListView.as_view(), name='products'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),  #нужно заменить на слаговую адресацию
    re_path(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    re_path(r'^product/<slug:product_slug>/$', ProductDetailView.as_view(), name="product_detail"), #не работает, кажется
]
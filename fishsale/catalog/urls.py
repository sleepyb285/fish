from django.urls import path, re_path
from . import views
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^products/$', views.ProductListView.as_view(), name='products'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
    path("<slug:slug>", ProductDetailView.as_view(), name="product_detail"),
]
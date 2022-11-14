from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('fish/<slug:slug>', views.FishDetailView, name = 'fish_detail'),
    path('category/<slug:slug>', views.CategoryDetailView, name = 'category_detail'),
    path('category/fish/<slug:slug>', views.FishDetailView, name = 'fish_detail' ),



    # re_path(r'^<slug:slug>$', views.CategoryDetailView.as_view(), name='category'),
    #re_path(r'^fish/<slug:slug>$', views.FishDetailView, name='fish-detail'),
]
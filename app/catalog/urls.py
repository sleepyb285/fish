from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('fish', views.FishDetailView.as_view(), name = 'fish-detail'),
    # re_path(r'^<slug:slug>$', views.CategoryDetailView.as_view(), name='category'),
    re_path(r'^fish/<slug:slug>$', views.FishDetailView.as_view(), name='fish-detail'),
]
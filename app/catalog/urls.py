from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('fish/<slug:slug>', views.FishDetailView, name = 'fish_detail'),
    path('<slug:slug>', views.CategoryDetailView, name = 'category_detail'),
    path('feedback', views.feedback, name = 'feedback' ),
    path('contacts', views.contacts, name = 'contacts' ),
    path('provider/<slug:slug>', views.ProviderDetailView, name = 'provider_detail' ),



    # re_path(r'^<slug:slug>$', views.CategoryDetailView.as_view(), name='category'),
    #re_path(r'^fish/<slug:slug>$', views.FishDetailView, name='fish-detail'),
]
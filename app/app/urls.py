"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from catalog.views import index,feedback,contacts, ProviderDetailView, LocationDetailView,nice,feedback_new, about, mst
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('feedback/', feedback, name = 'feedback' ),
    path('contacts/', contacts, name = 'contacts' ),
    path('catalog/',include('catalog.urls')),
    path('provider/<slug:slug>', ProviderDetailView, name = 'provider_detail'),
    path('contacts/<id>', LocationDetailView, name = 'location_detail'),
    path('nice/', nice, name = 'nice'),
    path('feedback/new/', feedback_new, name='feedback_new'),
    path('about/', about, name = 'about'),
    path ('mst/', mst, name = 'mst'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""basicDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.views.generic import TemplateView

from courses import views
from profiles import views as profiles_view
from homecoffee import views as coffee_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profiles_view.SiteLoginView.as_view(), name='login'),
    path('logout/', profiles_view.SiteLogoutView.as_view(), name='logout'),
    path('register/', profiles_view.SiteRegisterView.as_view(), name='register'),
    path('register/ok/', profiles_view.SiteRegisterOkView.as_view(), name='register_ok'),
    path('profile/', profiles_view.ProfileEditView.as_view(), name='profile'),

    path('homecoffee/', coffee_view.customer_reviews_view, name='homecoffee'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

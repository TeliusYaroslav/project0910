"""
URL configuration for order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import mainpage.views as mainpage_views
import productpage.views as productpage_views
import autoregister.views as autoregister_views
import contactpage.views as contactpage_views
import shoppingcardpage.views as shopping_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage_views.mainpage, name = "main"),
    path('productpage/', productpage_views.productpage, name = "productpage"),
    path('contactpage/',contactpage_views.contactpage, name = 'contactpage' ),
    path('autoregister', autoregister_views.autoregister, name = "autoregister"),
    path('shoppingcardpage', shopping_views.shopping, name = "shoppingcardpage")
]

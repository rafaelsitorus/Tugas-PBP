"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from products.views import show_xml, show_json, show_xml_by_id, show_json_by_id

from pages import views
from products.views import register, login_user, logout_user, edit_product, product_create_view, delete_mood

# app_name = "main2"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('form/', product_create_view),
    path('admin/', admin.site.urls),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-mood/<uuid:id>/', edit_product, name='edit_product'),
    path('product-create-view', product_create_view, name='product_create_view'),
    path('delete/<uuid:id>', delete_mood, name='delete_mood'),
]


from django.contrib import admin
from django.urls import path, include
from products.views import show_xml, show_json, show_xml_by_id, show_json_by_id

from pages import views
from products.views import product_create_view

# app_name = "main1"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('form/', product_create_view),
    path('admin/', admin.site.urls),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]

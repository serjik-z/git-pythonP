from django.urls import path
from . import views

urlpatterns = [
        path('about', views.index_about, name='about'),
        path('contact', views.contact_us, name='contact_us')
]
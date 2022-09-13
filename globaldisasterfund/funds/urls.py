from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('apply-for-funding/', views.apply_for_funding, name='apply_for_funds'),
    path('donate/', views.donate, name='donate'),
    path('resources/', views.resources, name='resources')
]

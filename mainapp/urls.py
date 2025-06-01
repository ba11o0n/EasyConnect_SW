from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-panel/', views.admin, name='admin'),
    path('vendor-panel/', views.vendor, name='vendor'),
    path('attendee-panel/', views.attendee, name='attendee'),
]

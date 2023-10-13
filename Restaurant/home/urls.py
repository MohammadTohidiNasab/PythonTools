from django.urls import path
from .views import HomePage, MenuView, AboutUs, ContactView

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('menu',MenuView.as_view(),name='menu'),
    path('about/',AboutUs.as_view(),name='about'),
    path('contact',ContactView.as_view(),name='contact'),
]

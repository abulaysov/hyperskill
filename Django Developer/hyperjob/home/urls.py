from django.urls import path
from .views import *
from django.views.generic import RedirectView


urlpatterns = [
    path('home', MyHomeView.as_view()),
    path('home/', RedirectView.as_view(url='/home')),
]
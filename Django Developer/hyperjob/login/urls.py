from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('login', MyLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
]

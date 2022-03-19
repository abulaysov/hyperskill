from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('signup', MySignupView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup'))
]
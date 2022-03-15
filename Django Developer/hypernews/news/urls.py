from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('news/<int:link>/', news),
    path('news/', mainpage),
    path('news/create/', create)
]
from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('vacancies/', VacancyPage.as_view()),
    path('vacancy/new', VacancyPage.as_view()),
    path('vacancy/new/', RedirectView.as_view(url='/vacancy/new'))
]
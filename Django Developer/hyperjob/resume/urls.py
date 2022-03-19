from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('resumes/', ResumePage.as_view()),
    path('resume/new', ResumePage.as_view()),
    path('resume/new/', RedirectView.as_view(url='/resume/new'))
]

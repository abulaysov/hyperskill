from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.http import HttpResponse


class VacancyPage(View):
    def get(self, request, *args, **kwargs):
        content = Vacancy.objects.all()
        return render(request, 'vacancy/vacancy.html', context={'data': content})

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponse(status=403)
        Vacancy.objects.create(description=request.POST.get('description'), author=request.user)
        return redirect('/home')
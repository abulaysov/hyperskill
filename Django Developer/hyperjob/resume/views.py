from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.http import HttpResponse


class ResumePage(View):
    def get(self, request, *args, **kwargs):
        content = Resume.objects.all()
        return render(request, 'resume/resume.html', context={'data': content})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse(status=403)
        Resume.objects.create(description=request.POST.get('description'), author=request.user)
        return redirect('/home')
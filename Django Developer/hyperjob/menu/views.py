from django.shortcuts import render
from django.views import View


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/index.html')

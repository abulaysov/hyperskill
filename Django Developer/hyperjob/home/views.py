from django.shortcuts import render
from django.views import View


class MyHomeView(View):
    def get(self, request, *args, **kwargs):
        content = {'auth': request.user.is_authenticated,
                   'staff': request.user.is_staff}
        return render(request, 'home/home.html', context=content)


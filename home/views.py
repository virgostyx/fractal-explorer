from django.views.generic import TemplateView
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('FRACTAL EXPLORER IS ALIVE')


class HomePageView(TemplateView):
    template_name = "home/home.html"

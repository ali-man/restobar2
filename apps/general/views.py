from django.shortcuts import render

from apps.general.models import Slider


def home_page(request):
    slider = Slider.objects.all()
    return render(request, 'home/index.html', locals())

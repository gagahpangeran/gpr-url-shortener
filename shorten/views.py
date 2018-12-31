from django.shortcuts import render, get_object_or_404
from .models import ShortenLink

# Create your views here.


def index(request):
    data = {} if not ShortenLink.objects.all(
    ) else {'data': ShortenLink.objects.all().order_by('-id')}
    return render(request, 'landing.html', data)


def get_link(request, slug):
    link = get_object_or_404(ShortenLink, slug=slug)
    return render(request, 'link.html', {'link': link})

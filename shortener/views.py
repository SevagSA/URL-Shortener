from django.shortcuts import render, redirect

from .forms import URLForm
from .models import ShortURL


def home(request):
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short_url = ShortURL.objects.create(url=url)
            form = URLForm(
                initial={'url': url, 'shortcode': short_url.shortcode})
    return render(request, 'shortener/home.html', {'form': form})


def go(request):
    shortcode = request.GET.get('code', None)
    if shortcode:
        url = ShortURL.objects.get(shortcode=shortcode).url
        return redirect(url)
    return render(request, 'shortener/go.html')

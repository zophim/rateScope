from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

@cache_page(60*5)
@vary_on_cookie
def index(request):
    context = {}
    context['objects'] = []
    return render(request, 'index.html', context)


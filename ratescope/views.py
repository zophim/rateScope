from django.shortcuts import render
from django.core.cache import cache

def index(request):
    context = {}
    objects = cache.get('objects_' + request.user.username + '_key')
    if not objects:
        objects = []
        cache.set('objects_' + request.user.username + '_key', 60 * 5)
    context['objects'] = []
    return render(request, 'index.html', context)


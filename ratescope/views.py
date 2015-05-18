from django.shortcuts import render

def index(request):
    context = {}
    context['objects'] = []
    return render(request, 'index.html', context)


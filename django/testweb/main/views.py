from django.shortcuts import render
# Create your views here.

def index(request):
    data = {
        'title':'Text_from_wiews',
        'values': ['suck', 'some', 'dick'],
        'dict': {'age': 18, 'name': 'Petya'}
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
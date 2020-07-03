from django.shortcuts import render


# Create your views here.

def television(request):
    return render(request, 'product/television.html')


def camera(request):
    return render(request, 'product/camera.html')


def ac(request):
    return render(request, 'product/ac.html')


def grinder(request):
    return render(request, 'product/grinder.html')

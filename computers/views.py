from django.shortcuts import render


# Create your views here.


def laptop(request):
    return render(request, 'product/laptop.html')


def desktop(request):
    return render(request, 'product/desktop.html')

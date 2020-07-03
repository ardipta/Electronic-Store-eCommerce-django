from django.shortcuts import render


# Create your views here.

def smartphone(request):
    return render(request, 'product/smartphone.html')


def mobilephone(request):
    return render(request, 'product/mobilephone.html')


def tablet(request):
    return render(request, 'product/tablet.html')

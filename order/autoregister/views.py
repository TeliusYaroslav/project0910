from django.shortcuts import render

# Create your views here.

def autoregister(request):
    return render(request, 'autoregister/index.html')
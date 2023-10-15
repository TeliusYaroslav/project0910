from django.shortcuts import render

# Create your views here.
def productpage(request):
    return render(request, 'productpage/productpage.html')
    
from django.shortcuts import render

# Create your views here.
def shopping(request):
    return render(request, 'shoppingcardpage/shopping.html')

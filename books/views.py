from django.shortcuts import render

# Create your views here.
def create_book(request):
    return render(request,'books/create.html')

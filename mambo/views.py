from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact.html')

def foodyard_view(request):
    return render(request, 'foodyard.html')

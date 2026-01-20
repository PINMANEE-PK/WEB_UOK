from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def water_factory(request):
    return render(request, 'water_factory.html')

def herbal_factory(request):
    return render(request, 'herbal_factory.html')

def cosmetic_factory(request):
    return render(request, 'cosmetic_factory.html')

def resort(request):
    return render(request, 'resort.html')

def room_detail(request):
    return render(request, 'room_detail.html')

def room_detail(request):
    return render(request, 'room_1a.html')

def room_2a_view(request):
    return render(request, 'room_2a.html')

def room_3a_view(request):
    return render(request, 'room_3a.html')

def room_4a_view(request):
    return render(request, 'room_4a.html')

def room_5a_view(request):
    return render(request, 'room_5a.html')
from django.shortcuts import render

# Create your views here.
def index_about(request):
    return render(request, 'about.html')
def contact_us(request):
    return render(request, 'about.html')
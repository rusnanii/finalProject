from django.shortcuts import render
def index(request):
    return render(request,'frontend/index.html')

def Earring(request):
    return render(request,'frontend/Earring.html')

def Necklace(request):
    return render(request,'frontend/Necklace.html')

def Bracelet(request):
    return render(request,'frontend/Bracelet.html')



# Create your views here.

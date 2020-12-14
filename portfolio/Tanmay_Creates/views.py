from django.shortcuts import render

def home_view(request):
    return render(request,'Tanmay_Creates/main.html',{})

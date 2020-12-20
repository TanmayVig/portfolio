from django.shortcuts import render
from django.http import JsonResponse

import json
from . import models

def home_view(request):
    project = models.Projects.objects.all()
    return render(request,'Tanmay_Creates/main.html',{'projects':project})

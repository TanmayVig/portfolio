from django.shortcuts import render
from django.http import JsonResponse


import json
from . import models
from . import forms

def home_view(request):
    project = models.Projects.objects.all()
    form = forms.PageForm

    if request.method == "POST":
        form = forms.PageForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = forms.PageForm

    return render(request,'Tanmay_Creates/main.html',{'projects':project,'form':form})

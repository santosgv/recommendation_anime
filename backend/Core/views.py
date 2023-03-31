from django.shortcuts import render
from .models import Recommend

def index(request):
    Posts = Recommend.objects.all()
    return render(request,'index.html',{'Posts':Posts})

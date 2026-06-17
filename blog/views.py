from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello ..welcome to Django")

def index(request):
    title='kiruba blog'
    return render(request,'blog/index.html',{'blog_title':title})

def detail(request,post_id):
    return render(request,'blog/detail.html')
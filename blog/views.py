from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello ..welcome to Django")

def index(request):
    title='kiruba blog'
    posts=[
        { 'id':1,'title' : 'post 1','content':'content of page 1' },
        { 'id':2,'title' : 'post 2','content':'content of page 2' },
        { 'id':3,'title' : 'post 3','content':'content of page 3' },
        { 'id':4,'title' : 'post 4','content':'content of page 4' },
    ]
    return render(request,'blog/index.html',{'blog_title':title, 'posts':posts})

def detail(request,post_id):
    return render(request,'blog/detail.html')
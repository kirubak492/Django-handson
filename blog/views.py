from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Post
logger = logging.getLogger(__name__)

# static post data
# posts=[
#         { 'id':1,'title' : 'Post 1','content':'Content of page 1' },
#         { 'id':2,'title' : 'Post 2','content':'Content of page 2' },
#         { 'id':3,'title' : 'Post 3','content':'Content of page 3' },
#         { 'id':4,'title' : 'Post 4','content':'Content of page 4' },
#     ]
# Create your views here.
def home(request):
    return HttpResponse("hello ..welcome to Django")

def index(request):
    title='kiruba blog'
    posts=Post.objects.all() #get post data using model
    return render(request,'blog/index.html',{'blog_title':title, 'posts':posts})

def detail(request,slug):
    # post=next((item for item in posts if item['id'] == int(post_id)),None)

    # logger.info(f'post value is {post}')

    # getting data from post by id
    post=Post.objects.get(slug=slug)

    return render(request,'blog/detail.html',{'post':post})
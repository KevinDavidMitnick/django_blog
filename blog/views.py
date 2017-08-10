from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('create_time')
    return render(request,'blog/index.html',context={'article_list' : article_list})

def about(request):
    return render(request,'blog/about.html')

def blog_post(request):
    return render(request,'blog/post.html')

def contact(request):
    return render(request,'blog/contact.html')

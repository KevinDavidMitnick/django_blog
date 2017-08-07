from django.shortcuts import render,get_object_or_404
from .models import Article
import markdown

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('create_time')
    return render(request,'blog/index.html',context={'article_list' : article_list})

def about(request):
    return render(request,'blog/about.html')

def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.content = markdown.markdown(article.content,extensions= [
        'markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
    return render(request,'blog/post.html',context={'article' : article})

def contact(request):
    return render(request,'blog/contact.html')

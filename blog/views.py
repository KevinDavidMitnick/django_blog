from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Category
import markdown
from comments.forms import CommentForm

# Create your views here.
def index(request,cid=-1):
    if cid == -1:
        article_list = Article.objects.all().order_by('-create_time')[:8]
    else:
        category = get_object_or_404(Category,pk=cid)
        article_list = Article.objects.filter(category=category).order_by('-create_time')[:8]
    return render(request,'blog/index.html',context={'article_list':article_list})

def about(request):
    return render(request,'blog/about.html')

def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.content = markdown.markdown(article.content,extensions= [
        'markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
    form = CommentForm(request.POST)
    comment_list = article.comment_set.all()
    context = { 'article' : article,
                'form' : form,
                'comment_list' : comment_list}
    return render(request,'blog/post.html',context=context)

def contact(request):
    return render(request,'blog/contact.html')

from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Category
import markdown
from comments.forms import CommentForm

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def index(request,cid=-1):
    if cid == -1:
        article_list = Article.objects.all().order_by('-create_time')
    else:
        category = get_object_or_404(Category,pk=cid)
        article_list = Article.objects.filter(category=category).order_by('-create_time')
    paginator = Paginator(article_list,3)
    page = request.GET.get('page')
    try:
        pager = paginator.page(page)
    except PageNotAnInteger:
        pager = paginator.page(1)
    return render(request,'blog/index.html',context={'pager':pager})

def about(request):
    return render(request,'blog/about.html')

def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.increase_readcnt()
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

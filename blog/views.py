from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Category,Tag
import markdown
from comments.forms import CommentForm
from markdown.extensions.toc import TocExtension

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils.text import slugify

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-create_time')
    paginator = Paginator(article_list,3)
    page = request.GET.get('page')
    try:
        pager = paginator.page(page)
    except PageNotAnInteger:
        pager = paginator.page(1)
    return render(request,'blog/index.html',context={'pager':pager})

def category(request,cid):
    category = get_object_or_404(Category,pk=cid)
    article_list = category.article_set.order_by('-create_time')
    paginator = Paginator(article_list,3)
    page = request.GET.get('page')
    try:
        pager = paginator.page(page)
    except PageNotAnInteger:
        pager = paginator.page(1)
    return render(request,'blog/index.html',context={'pager':pager})

def tag(request,tid):
    tag = get_object_or_404(Tag,pk=tid)
    article_list = tag.article_set.order_by('-create_time')
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
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)
    ])
    article.content = md.convert(article.content)
    article.toc = md.toc
    form = CommentForm(request.POST)
    comment_list = article.comment_set.all()
    context = { 'article' : article,
                'form' : form,
                'comment_list' : comment_list}
    return render(request,'blog/post.html',context=context)

def contact(request):
    return render(request,'blog/contact.html')

from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Category,Tag,Author
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

def write(request):
    if request.method == "POST":
        category_name = request.POST.get("category")
        category,_ = Category.objects.get_or_create(name=category_name)

        tag_name = request.POST.get("tag")
        tag,_ =  Tag.objects.get_or_create(name=tag_name)

        username = request.user.username
        password = request.user.password
        email = request.user.email
        author,_ = Author.objects.get_or_create(name=username,password=password,email=email)

        article = Article()
        article.category = category
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.author = author
        article.save()
        article.tags.add(tag)
        article.save()
        return redirect(article)
    else:
        return render(request,'blog/write.html')

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
    comment_list = article.comment_set.all()
    context = { 'article' : article,
                'comment_list' : comment_list}
    return render(request,'blog/post.html',context=context)

def contact(request):
    return render(request,'blog/contact.html')

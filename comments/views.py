from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Article
from .models import Comment

# Create your views here.
def post_comment(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text').strip(' ')
        if text !="":
            comment =  Comment()
            comment.article = article
            comment.author = request.user
            comment.text = text
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            context = { 'article' : article,
                        'comment_list' : comment_list}
            return render(request,'blog/post.html',context=context)
    return  redirect(article)



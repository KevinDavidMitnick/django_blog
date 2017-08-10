from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def about(request):
    return render(request,'blog/about.html')

def blog_post(request):
    return render(request,'blog/post.html')

def contact(request):
    return render(request,'blog/contact.html')

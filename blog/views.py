from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Template
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    #return HttpResponse("testingggggg")
    template = loader.get_template('blog/index.html')
    try:
        context={'none':'none'}
        return HttpResponse(template.render(context,request))
    except:
        return HttpResponse("tempalte not found")


def post_list(request):
    posts = Post.objects.filter(title__contains='t')
    return render(request, 'blog/post_list.html', {'posts':posts})
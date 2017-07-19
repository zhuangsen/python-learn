# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog


# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello world</h1>')


def showBlog(request, blogId):
    t = loader.get_template('blog.html')
    blog = Blog.object.get(id=blogId)
    context = {'blog': blog}
    html = t.render(context)
    return HttpResponse(html)


def showBlogList(request):
    t = loader.get_template('blog_list.html')
    blogs = Blog.object.all()
    context = {'blogs': blogs}
    html = t.render(context)
    return HttpResponse(html)

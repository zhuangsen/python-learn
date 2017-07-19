# -*- coding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.advanced/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from blog.views import hello
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # django 1.10以前的写法
    # url(r'hi', 'blog.views.hello'),
    # django 1.10以后的写法 from blog.views import hello
    # url(r'hi', hello)
    url(r'hi', views.hello),
    url(r'^$', views.showBlogList),
    url(r'^blog/(\d+)$', views.showBlog),
]

# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import json

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

from datetime import date, datetime

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError('Type %s not serializable' % type(obj))

def get_post_list(self):
    posts = Post.objects.filter(published_date__lte=date.today()).order_by('published_date')
    return posts

def base(request):
    posts = get_post_list(None);
    return render(request, 'blog/base.html', {'posts': posts})

def about_me(request):
    return render(request, 'blog/about.html')

def post_list(request):
    posts = getPostList()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_recent(request):
    posts = Post.objects.filter(published_date__lte=date.today()).latest('published_date')
    return render(request, 'blog/post_recent.html', {'post': posts})

def post_detail(request, pk):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=pk)
        post_list = get_post_list(None)

        return render(request, 'blog/post_detail.html', {'post': post, 'post_list': post_list})

    else:
        return HttpResponse(
            json.dumps({'post error': 'A problem occurred looking for the post'}),
            content_type = 'application/json'
        )

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = date.today()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = date.today()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

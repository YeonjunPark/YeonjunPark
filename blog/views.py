from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommentModelForm
from .models import Post, Comment

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
        })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = Comment.objects.filter(post=post)

    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'comment_list' : comment_list,
        })


def self_introduction(request):
    return render(request, 'blog/self_introduction.html', {})

def mysum(request, x):
    return HttpResponse(sum(int(i) for i in x.split('/') if i))

def comment_new(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm()

    return render(request, 'blog/comment_form.html', {
        'form': form,
        })

def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm(instance=comment)

    return render(request, 'blog/comment_form.html', {
        'form': form,
        })
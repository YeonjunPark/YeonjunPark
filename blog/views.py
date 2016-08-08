from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import CommentModelForm, CommentForm
from .models import Post, Comment

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
        })

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DeosNotExist:
    #     raise Http404

    post = get_object_or_404(Post, pk=pk)

    comment_list = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        comment_form = CommentForm()


    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_list': comment_list,
        'comment_form': comment_form,
        })


def self_introduction(request):
    return render(request, 'blog/self_introduction.html', {})

def mysum(request, x):
    return HttpResponse(sum(int(i) for i in x.split('/') if i))

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES) # 파일 업로드 받을 때에는 필히 request.FILES 지정하기 !!!
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # return redirect('/blog/') 블로그 홈페이지로 가는 것
            # return redirect('blog.views.post_detail', post.pk)
            return redirect(post)
            # return redirect(post.get_absolute_url())
            # return redirect('/2/')
    else:
        form = CommentModelForm()

    return render(request, 'blog/comment_form.html', {
        'form': form,
        })

def comment_edit(request, post_pk, pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(post)
    else:
        form = CommentModelForm(instance=comment)

    return render(request, 'blog/comment_form.html', {
        'form': form,
        })
from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

def self_introduction(request):
    return render(request, 'blog/self_introduction.html', {})
from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def self_introduction(request):
    return render(request, 'blog/self_introduction.html', {})

def mysum(request, x):
    return HttpResponse(sum(int(i) for i in x.split('/') if i))



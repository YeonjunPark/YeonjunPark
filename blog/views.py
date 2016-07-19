from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def self_introduction(request):
    return render(request, 'blog/self_introduction.html', {})

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x) + int(y) + int(z))



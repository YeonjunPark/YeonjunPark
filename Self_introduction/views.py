from django.shortcuts import render

# Create your views here.
def self_introduction(request):
    return render(request, 'blog/self_introduction.html', {})
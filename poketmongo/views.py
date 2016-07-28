from django.shortcuts import render
from poketmongo.models import Poketmon, User, Capture


def poketmon_list(request):
    qs = Poketmon.objects.all()
    return render(request, 'poketmongo/poketmon_list.html', {
        'poketmon_list': qs
        })

def user_list(request):
    user_list = User.objects.all()
    return render(request, 'poketmongo/user_list.html', {
        'user_list': user_list
        })

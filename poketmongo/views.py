from django.shortcuts import render
from poketmongo.models import Poketmon


def poketmon_list(request):
    qs = Poketmon.objects.all()
    return render(request, 'poketmongo/poketmon_list.html', {
        'poketmon_list': qs
        })
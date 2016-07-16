from django.shortcuts import render


def poketmon_user_list(request):
    return render(request, 'potetmongo/poketmon_user_list', {})
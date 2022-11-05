

from django.shortcuts import render


def create_wish(request):
    print('here')
    return render(request, "wish/wish.html", {})

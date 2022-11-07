from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Q

from .forms import WishForm
from .models import Wish


@login_required
def create_wish(request):
    if request.method == 'POST':
        form = WishForm(request.POST or None)

        if form.is_valid():
            wish = form.save(commit=False)
            wish.author = request.user
            wish.save()
            my_items = Wish.objects.filter(author=request.user)
            all_items = Wish.objects.filter(~Q(author=request.user))
            messages.success(request, ("Your location that you want to visit has been added to List !"))
            return render(request, "wish/wish.html", {'all_items': all_items, 'my_items': my_items})

    else:
        my_items = Wish.objects.filter(author=request.user)
        all_items = Wish.objects.filter(~Q(author=request.user))
        return render(request, "wish/wish.html", {'all_items': all_items, 'my_items': my_items})


@login_required
def delete(request, wish_id):
    item = Wish.objects.get(pk=wish_id)
    if item.author == request.user:
        item.delete()
        messages.success(request, ('Location Has Been Deleted !'))
    else:
        messages.error(request, ('You are not allowed to delete other user\'s wishes'))
    return redirect('wish_create')


@login_required
def cross_off(request, wish_id):
    item = Wish.objects.get(pk=wish_id)
    if item.author == request.user:
        item.completed = True
        item.save()
    else:
        messages.error(request, ('You are not allowed to change other user\'s wishes'))
    return redirect('wish_create')


@login_required
def uncross(request, wish_id):
    item = Wish.objects.get(pk=wish_id)
    if item.author == request.user:
        item.completed = False
        item.save()
    else:
        messages.error(request, ('You are not allowed to change other user\'s wishes'))
    return redirect('wish_create')
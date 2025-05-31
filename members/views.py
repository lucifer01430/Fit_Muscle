from django.shortcuts import render, redirect
from .models import Membership
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import date, timedelta

@login_required
def dashboard(request):
    user = request.user
    try:
        membership = Membership.objects.get(user=user)
    except Membership.DoesNotExist:
        membership = None

    return render(request, 'members/dashboard.html', {
        'membership': membership
    })

@login_required
def buy_membership(request):
    if request.method == 'POST':
        plan = request.POST.get('plan')
        duration_days = 30  # default validity
        start = date.today()
        end = start + timedelta(days=duration_days)

        Membership.objects.update_or_create(
            user=request.user,
            defaults={'plan': plan, 'start_date': start, 'end_date': end, 'is_active': True}
        )
        return redirect('dashboard')

    return render(request, 'members/buy_membership.html')


def register(request):
    return render(request, 'members/register.html')


def user_login(request):
    return render(request, 'members/login.html')


def user_logout(request):
    logout(request)
    return redirect('home') 
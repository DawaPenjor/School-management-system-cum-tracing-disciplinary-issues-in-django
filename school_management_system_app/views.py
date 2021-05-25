from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(
                request, 'Username and password didnot match. Try again!')
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect('adm_home')
    else:
        return render(request, 'login.html')


@ login_required
def logoutuser(request):
    logout(request)
    return redirect('loginuser')

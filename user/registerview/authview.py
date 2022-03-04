from tkinter import N
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login

from user.form import CustomUserForm

def Register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print('working1')
        if form.is_valid():
            print('working2')
            form.save()
            messages.success(
                request, "Registration  Successfully Loging to continue")
            return redirect('/login')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    print('number1')
    if request.user.is_authenticated:
        messages.warning(request, "your already logging")
        return redirect('/')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=name, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "login Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invaliv Username or password")
                return redirect("/")
        print("helo 1")

        return render(request, 'master.html')

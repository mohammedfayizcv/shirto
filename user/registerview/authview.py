from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from user.form import CustomUserForm

def Register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print('working1')
        if form.is_valid():
            print('working2')
            form.save()
            # send_mail(
            #    'Appointment is Registered',
            #     "This Appointment is registered,  "+form.username+"  We will inform you shortly via the next email to confirm your Token Number and Appoinment Time.",
            #     'fayizcv1@gmail.com',   
            #     [form.email],
            #     fail_silently=False,
            # )
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
        return render(request, 'login.html')


def logoutpage(request):
    print('logout first')
    
    if request.user.is_authenticated:
        print('logout')
        logout(request)
        messages.success(request, "logged out Successfully")
    return redirect('/')
        
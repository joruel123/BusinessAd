from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import RegistrationForm, LoginForm

# Create your views here.
@login_required
def index(request):
    if not request.user.is_staff:
        return render(request, 'application/index.html')
    else:
        return redirect('application:administrator')

def register(request):
    form = RegistrationForm()

    if request.method == 'GET':
        return render(request, 'registration/register.html', {
            'form': form
        })
    elif request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'registration/register.html', {
                'form': RegistrationForm(),
                'success': 'You have successfully registered.'
            })
        else:
            return render(request, 'registration/register.html', {
                'form': form
            })

def user_logout(request):
    logout(request)
    return redirect('application:index')

def user_login(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'registration/login.html', {
            'form': form
        })
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth = authenticate(username=username, password=password)

        if auth is not None:
            if auth.is_staff:
                login(request, auth)
                return redirect('application:administrator')

            if auth.is_approve and not auth.is_staff:
                login(request, auth)
                return redirect('application:index')

            else:
                return render(request, 'registration/login.html', {
                    'form': form,
                    'error': 'You are still for approval.',
                })
        else:
            return render(request, 'registration/login.html', {
                'form': form,
                'error': 'Please enter a correct username and password. Note that both fields may be case-sensitive.',
            })
@login_required
def administrator(request):
    if request.method == 'GET':
        if request.user.is_staff:
            users = CustomUser.objects.all().filter(
                is_approve=False, 
                is_complete=False, 
                is_staff=False
            )
            return render(request, 'application/administrator.html', {
                'users': users
            })
        else:
            return redirect('application:index')

def approval(request, id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=id)
        user.is_approve = True
        user.is_complete = True
        user.save()

        users = CustomUser.objects.all().filter(
            is_approve=False, 
            is_complete=False, 
            is_staff=False
        )

        return render(request, 'application/administrator.html', {
            'users': users
        })

def disapproval(request, id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=id)
        user.is_complete = True
        user.save()

        users = CustomUser.objects.all().filter(
            is_approve=False, 
            is_complete=False, 
            is_staff=False
        )

        return render(request, 'application/administrator.html', {
            'users': users
        })
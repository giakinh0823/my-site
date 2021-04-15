from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm, UserForm


# Create your views here.

@user_passes_test(lambda u: u.is_anonymous, login_url='home:index')
def loginuser(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'register/login.html',
                          {'form': AuthenticationForm(), 'error': "Username or Password wrong"})
        else:
            login(request, user)
            return redirect('home:index')
    return render(request, 'register/login.html', {'form': AuthenticationForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect('home:index')


@user_passes_test(lambda u: u.is_anonymous, login_url='home:index')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:index')
        else:
            return render(request, 'register/signup.html', {'form': form, 'error': 'Please input is valid'})
    else:
        form = SignUpForm()
        return render(request, 'register/signup.html', {'form': form})


@login_required
def editname(request):
    form = UserForm(instance=request.user)
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        user = form.save(commit=False)
        user.save()
    return render(request, 'register/editname.html', {'form': form})

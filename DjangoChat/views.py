from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.contrib import messages

from .forms import LoginForm, RegisterForm

from .models import User

from django.contrib.auth.decorators import login_required



def view_404(request):

    return HttpResponseRedirect('/login')



def index(request):

    return HttpResponseRedirect('/login')



def login_view(request):

    form = LoginForm(request.POST or None)

    context = {

        'title': 'Login',

        'form': form

    }

    msgs = messages.get_messages(request)

    for msg in msgs:

        context['success'] = msg



    if form.is_valid():

        email = form.cleaned_data.get('email')

        password = form.cleaned_data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:

            login(request, user)

            return HttpResponseRedirect('/lobby')

        else:

            print("Username: " + email)

            print("Password: " + password)

            context['error'] = 'Invalid credentials'



    return render(request, "login_register_form.html", context)



def register(request):

    form = RegisterForm(request.POST or None)

    context = {

        'title': 'Register',

        "form": form

    }



    if form.is_valid():

        username = form.cleaned_data.get("username")

        email = form.cleaned_data.get("email")

        password = form.cleaned_data.get("password")

        User.objects.create_user(email, username, password)



    if request.method == 'POST':

        if form.errors:

            if form.non_field_errors():

                context['error'] = form.non_field_errors()

                print(context['error'])

                print('YAY')

            for field in form.fields:

                if form.errors.get(field, False):

                    context['error'] = form.errors[field]

                    print(context['error'])

                    print('NAY')

                    break

        else:

            messages.success(request, 'You have successfuly registered!')

            return HttpResponseRedirect('/login')



    return render(request, "login_register_form.html", context)



@login_required

def logout_handler(request):

    # well it should not be a get method

    if request.method == 'GET':

        logout(request)

    return HttpResponseRedirect('/login')
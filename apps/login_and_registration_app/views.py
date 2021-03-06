from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request, "login_and_registration_app/index.html")

def validate_registration(request):
    if request.method == 'POST':
        postData = request.POST
        context = User.objects.register_validate(postData)
        if context['error_message']:
            for err_msg in context['error_message']:
                messages.add_message(request, messages.ERROR, err_msg)
            # return render(request, "login_and_registration_app/index.html")
            return redirect('/')
        if context['success_message']:
            for success_msg in context['success_message']:
                messages.add_message(request, messages.SUCCESS, success_msg)
            user = User.objects.get(username=request.POST['username'])
            request.session['id']= user.id
            # return render(request, "login_and_registration_app/success.html", context)
            return redirect('/success')
        else:
            return redirect('/')

def validate_login(request):
    if request.method == 'POST':
        postData = request.POST
        username = request.POST['username']
        user = User.objects.filter(username=username)

        print "*"*42
        print user
        print "*"*42

        context = User.objects.login_validate(postData)
        if context['error_message']:
            for err_msg in context['error_message']:
                messages.add_message(request, messages.ERROR, err_msg)
            # return render(request, "login_and_registration_app/index.html")
            return redirect('/')
        if context['success_message']:
            for success_msg in context['success_message']:
                messages.add_message(request, messages.SUCCESS, success_msg)
            # firstname = user.first_name

            request.session['id'] = context['user'].id
            # return render(request, "login_and_registration_app/success.html", context)
            return redirect('/success')
        else:
            return redirect('/')

def success(request):
    return redirect('/travel_dashboard')

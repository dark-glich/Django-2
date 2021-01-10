from django.shortcuts import render, redirect
from django import forms 
from .forms import register
from .models import form 

def SignupView(request, *args, **kwargs):
    signup_form = register(request.POST or None)
    created, email = None, None
    
    if signup_form.is_valid():
        obj, created = form.objects.get_or_create(email=signup_form.cleaned_data['email'])
        #obj.first_name = signup_form.cleaned_data['first_name']
        #obj.last_name = signup_form.cleaned_data['last_name']
        email = signup_form.cleaned_data['email']
        if created == True:
            obj.delete()
            signup_form.save()
            signup_form = register()
            return redirect('list')

    context = {
        'form': signup_form,
        'created':created, 
        'email':email
    }
    return render(request, 'signup.html', context)

def SigninView(request, *args, **kwargs):
    sign_form = register(request.POST or None)
    created, email = None, None
    if sign_form.is_valid():
        email = sign_form.cleaned_data['email']
        obj, created = form.objects.get_or_create(email=sign_form.cleaned_data['email'],password=sign_form.cleaned_data['password'])
        if created == True:
            obj.delete()

        else:
            sign_form = register()
            return redirect('list')

    context={
        'form':sign_form, 
        'created':created, 
        'email':email
    }
    return render(request, 'signup2.html', context)


from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """register a new user."""
    if request.method !='POST':
        #DISPLAY A BLANK REGISTRATION FORM.
        form =UserCreationForm()
    else:
        #Process completed form.
        form =UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            #log the user in and then redirect to home page.
            login(request,new_user)
            return redirect('learning_logs:index')
    #DISPLAY A BLANK OR INVALID FORM.
    context={'form':form}
    return render(request,'registration/register.html',context)
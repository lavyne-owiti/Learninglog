from this import s
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email =forms.EmailField(required=True)
    # firstname =forms.CharField(max_length=15)
    # lastname=forms.CharField(max_length=15)

    class Meta:
        model= User
        fields =("firstname","lastname","username","email","password","password1")

    def save(self,commit=True):
        user =super(UserForm,self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user
      
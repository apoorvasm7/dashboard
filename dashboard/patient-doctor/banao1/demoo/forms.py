from django.db import models  
from django.forms import fields  
from demoo.models.user import User
from django import forms  
  
class UserImage(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = User  
        # It includes all the fields of model  
        fields = ('fname', 'lname', 'photo', 'uname', 'email', 'password', 'address') 
        labels={
            'fname': '',
            'lname': '',
            'photo': '',
            'uname': '',
            'email': '',
            'password': '',
            'address': '',
        }
        widgets={}
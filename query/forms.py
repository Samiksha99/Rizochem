from django import forms
from django.forms import ModelForm
from query.models import Message

class MessageForm(ModelForm):

    class Meta:
        model = Message

        fields=['first_name','last_name','email','content']        

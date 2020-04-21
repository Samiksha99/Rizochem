from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
# Create your views here.

def contact(request): 
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            message = Message(first_name=first_name, last_name=last_name, email=email, content=content)
            message.save()
        return redirect('/')
    else:
        return render(request,"contact.html")
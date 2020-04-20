from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, "index.html")

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        user = User.objects.create_user(name=name, email=email, query=query)
        user.save();
        print('Query sent')
        return redirect('/')

    else:
        return render(request, "index.html")


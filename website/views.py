from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import MessageForm, RegisterForm, ResponseForm
from .models import Message, User, Response


# Create your views here.


def index(request):

    context = {
        "message": "coucou"
    }
    return render(request, 'website/home.html', context)


def bidule(request):

    return render(request, 'website/bidule.html', {"bidule": "un nouveau message"})


def all_messages(request):
    messages = Message.objects.all()
    context = {"messages":messages}

    return render(request, 'website/all.html', context)


def show_message(request, id):

    message = Message.objects.get(id=id)
    responseForm = ResponseForm()

    return render(request, 'website/show.html', {"message": message, "responseForm": responseForm})

@login_required(login_url='login')
def new_message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect('show_message', message.id)


    return render(request, 'website/new_message.html',{'form' : form})


@login_required(login_url='login')
def edit_message(request, id):
    message = Message.objects.get(id=id)
    if message.author != request.user:
        return redirect('all_messages')
    form = MessageForm(instance=message)
    if request.method == 'POST':
        form = MessageForm(data=request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('show_message', message.id)
    return render(request, 'website/edit_message.html',{'form' : form,'message': message})
@login_required(login_url='login')

def delete_message(request, id):
    message = Message.objects.get(id=id)
    if message.author != request.user:
        return redirect('all_messages')
    message.delete()
    return redirect('all_messages')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            return redirect('all_messages')

    return render(request, 'website/register.html', {"form":form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return redirect('all_messages')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('all_messages')

    return render(request, 'website/login.html')


def logout_user(request):
    logout(request)
    return redirect('all_messages')

@login_required(login_url='login')

def add_response(request, id):
    message = Message.objects.get(id=id)
    if message is None:
        return redirect('all_messages')
    if request.method == 'POST':
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.message = message
            response.author = request.user
            response.save()

    return redirect('show_message', message.id)
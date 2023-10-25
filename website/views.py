from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import MessageForm
from .models import Message


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

    return render(request, 'website/show.html', {"message":message})


def new_message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('show_message', message.id)


    return render(request, 'website/new_message.html',{'form' : form})


def edit_message(request, id):
    message = Message.objects.get(id=id)
    form = MessageForm(instance=message)
    if request.method == 'POST':
        form = MessageForm(data=request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('show_message', message.id)
    return render(request, 'website/edit_message.html',{'form' : form,'message': message})

def delete_message(request, id):
    message = Message.objects.get(id=id)
    message.delete()
    return redirect('all_messages')

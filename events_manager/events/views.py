from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Event


def index(request):
    events = Event.objects.all()

    context = {
        'events':events
    }
    return render(request, 'index.html', context)


def details(request, id):
    event = Event.objects.get(id=id)

    context = {
        'event':event
    }
    return render(request, 'details.html', context)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        date = request.POST['date']
        duration = request.POST['duration']

        event = Event(title=title, text=text, date=date, duration=duration)

        messages.success(request,"Successfully Created")

        event.save()

        return redirect('/events')
    else:
        messages.error(request,"Something went wrong...")

        return render(request, 'add.html')


def edit(request, id):

    event = Event.objects.get(id=id)

    context = {
        'event':event
    }

    return render(request, 'edit.html', context)


def update(request, id):
    event = Event.objects.get(id=id)

    event.title = request.POST['title']
    event.text = request.POST['text']
    event.date = request.POST['date']
    event.duration = request.POST['duration']

    messages.success(request,"Successfully Updated")

    event.save()

    return redirect('/events')


def delete(request, id):

    event = Event.objects.get(id=id)

    event.delete()

    messages.success(request,"Successfully Deleted")

    return redirect('/events')

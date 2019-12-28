from django.shortcuts import render,redirect

from django import forms
from .models import Feed_Message

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

def hello_world(request):
    return render(request, 'template_whoami.html',{
        'now': str(datetime.today()),
    })

def index(request):
    return render(request, 'test2.html', {
        'name' : "K e v i n __ C h e n g",

    })

def bio(request):
    return render(request, 'bio.html',{

    })

def work(request):
    return render(request, 'work.html',{

    })

def contact(request):
    return render(request, 'contact.html',{

    })
def test(request):
    return render(request, 'anotherwork.html',{

    })

def test2(request):
    return render(request, 'test2.html',{

    })



class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed_Message
        fields = ['email','subject','message']

def post_create_feedback(request):
    if request.method=='POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            new_feed = form.save()
            print(new_feed)
            return redirect('/bio')
        else:
            return redirect('/feedback/post')

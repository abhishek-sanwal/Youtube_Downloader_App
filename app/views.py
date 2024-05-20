from django.shortcuts import render
from pytube import *
# Create your views here.

import pyperclip

def copy_from_clipboard():

    text = pyperclip.paste()

    return text

def index(request):

    if request.method == "POST":

        link = request.POST["link"]

        video = YouTube(link)

        title, views, length = video.title , video.views, video.length
  
        # setting video resolution 
        stream = video.streams.get_lowest_resolution() 
          
        # downloads video 
        stream.download() 

        return render(request, 
                      template_name="index.html",
                      context={
                        "title":title,
                        "views":views,
                        "length" : length
        })

    return render(request,template_name="index.html",
                  context={
                      "length":0,
                  })
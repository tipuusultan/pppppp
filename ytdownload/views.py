from django.shortcuts import render
from pytube import YouTube
from .models import videos
import os
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        yt = YouTube(url)
        filename = yt.title.replace(' ','%20')
        cwd = os.getcwd()
        videofile = yt.streams.all().first().download(f'{cwd}/media/ytdownloaded/')
        # print("Succesfully download")
        
        parse = {
            "filename": filename,
            "site":get_current_site(request),
        }
        return render(request, 'download.html', parse)
    else:
        return render(request, 'download.html')

    # https://www.youtube.com/watch?v=jrUTNfcOmvw

# def download(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         yt = YouTube(url)
#         filename = yt.title.replace(' ','%20')
#         videofile = yt.streams.first().download('E:/PYTHON PROJECTS + PRACTISE/imageupload/media/ytdownloaded/')
#         print("Succesfully download")
#         parse = {
#             "filename": filename
#         }
#     return render(request, 'download.html' , parse)

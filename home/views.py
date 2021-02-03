from django.shortcuts import render
from .models import Image, Video
from .forms import ImageForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Image(photo='/ff.jpg')
        form.save()
    form = ImageForm()
    images = Image.objects.all()
    videos = Video.objects.all()
    context = {
        "form": form,
        'image': images,
        'video':videos,
    }
    return render(request , 'index.html' , context)
    

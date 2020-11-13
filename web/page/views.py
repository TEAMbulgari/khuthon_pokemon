from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,FileResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
import base64
# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES['photo']:
        upload_file = request.FILES['photo']
        media_dir = 'media/page/files/'
        fs = FileSystemStorage(location=media_dir)
        fs.save(upload_file.name, upload_file)
    return render(request, 'index.html')

def upload(request):
    return render(request, 'upload.html')

def webcam(request):
    return render(request, 'webcam.html')

def show(request):
    return render(request, 'show.html')

@csrf_exempt
def canvasToImage(request):
    data = request.POST.__getitem__('data')
    data = data[39:]
    data += '=' *(4 - len(data) % 4)
    path = 'media/page/files/'
    filename = 'image.jpg'
    image = open(path+filename, "wb")
    image.write(base64.b64decode(data))
    image.close()
    return getResult()

def getResult():
    return HttpResponseRedirect(reverse('index'))

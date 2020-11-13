from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES['photo']:
        upload_file = request.FILES['photo']
        media_dir = 'media/page/files/'
        fs = FileSystemStorage(location=media_dir)
        fs.save(upload_file.name, upload_file)
    return render(request, 'index.html')


def show(request):
    return render(request, 'show.html')

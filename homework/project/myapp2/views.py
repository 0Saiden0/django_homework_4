from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
import logging




logger = logging.getLogger(__name__)


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    
    return render(request, 'myapp2/upload_image.html',{'form':form})
        



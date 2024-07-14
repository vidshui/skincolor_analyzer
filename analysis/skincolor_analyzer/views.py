from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo
from .utils import analyze_skin_tone

def home(request):
    return render(request, 'skincolor_analyzer/home.html')

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            skin_category = analyze_skin_tone(photo.image.path)
            photo.skin_category = skin_category
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'skincolor_analyzer/upload_photo.html', {'form': form})

def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    return render(request, 'skincolor_analyzer/photo_detail.html', {'photo': photo})

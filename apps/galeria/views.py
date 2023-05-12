from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Photography
from apps.galeria.forms import PhotographyForms
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('login')
    
    photographys = Photography.objects.order_by("date_picture").filter(published=True)
    return render(request, "galeria/index.html", {"cards": photographys})


def imagem(request, picture_id):
    picture = get_object_or_404(Photography, pk=picture_id)
    return render(request, "galeria/imagem.html", {"photography": picture})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('login')
    
    photographys = Photography.objects.order_by("date_picture").filter(published=True)
    if "search" in request.GET:
        search_name = request.GET["search"]
        if search_name:
            photographys = photographys.filter(name__icontains=search_name)
    return render(request, "galeria/search.html", {"cards": photographys})

def new_image(request):
    
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('login')
    
    form = PhotographyForms
    if request.method == 'POST':
        form = PhotographyForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Image published successfully")
            return redirect('galeria/index.html')
    return render(request, 'galeria/new_image.html', {'form': form})

def edit_image(request):
    pass

def delete_image(request):
    pass
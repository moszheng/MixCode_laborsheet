from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadModelForm
from .models import Post

def get_name(request):

    template_name = 'index/index.html'

    if request.method == 'POST':
        
        form = UploadModelForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()            
            return HttpResponseRedirect('/thanks/')   
    
    else:
        form = UploadModelForm()
    
    return render(request, template_name, {'form': form})

def thanks(request):

    html_name = 'thanks.html'
    return render(request, html_name)
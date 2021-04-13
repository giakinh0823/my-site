from django.shortcuts import render
from comment import forms
from comment.forms import CommentForm

# Create your views here.

  

def home(request):
    return render(request, 'home/index.html')  


def addComment(request):
    if request.POST:
        form_comment = CommentForm(data=request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
                comment.save()
        else:
            raise forms.ValidationError("wrong format")
    return render(request, 'home/index.html', {'commentForm': CommentForm()})

def handler404(request,exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
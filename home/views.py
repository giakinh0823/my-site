from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render

from comment import forms
from comment.forms import CommentForm


# Create your views here.


def home(request):
    name = "Hello"
    if request.user.is_authenticated:
        name = request.user.get_full_name()
    return render(request, 'home/index.html', {'commentForm': CommentForm(), 'name': name})


def addComment(request):
    if request.method == "POST":
        form_comment = CommentForm(data=request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            subject = form_comment.cleaned_data['title']
            body = {
                'Username': 'User:' + str(request.user),
                'Fullname': 'Name:' + form_comment.cleaned_data['name'],
                'Email': 'From: ' + form_comment.cleaned_data['email'],
                'Message': 'Message: ' + form_comment.cleaned_data['content'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'giakinhfullstack@gmail.com', ['giakinh2000@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        else:
            raise forms.ValidationError("wrong format")
    return render(request, 'home/index.html', {'commentForm': CommentForm()})



def handler404(request,exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

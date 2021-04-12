from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def index(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', context)


def fullposts(request, id):
    blogs = BlogPost.objects.get(pk=id)
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/fullposts.html', context)


def blogs_posts(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/posts.html', context)


def dashboard(request):
    if request.user.is_authenticated:
        blogs = BlogPost.objects.all()
        context = {
            'blogs': blogs,
        }
        return render(request, 'blog/dashboard.html', context)
    else:
        return HttpResponseRedirect('/signin/')


def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = BlogPost.objects.get(pk=id)
            forms = BlogPostForm(request.POST, instance=pi)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = BlogPost.objects.get(pk=id)
            forms = BlogPostForm(instance=pi)
        context = {
            'forms': forms,
        }
        return render(request, 'blog/editpost.html', context)
    else:
        return HttpResponseRedirect('/signin/')


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = BlogPost.objects.get(pk=id)
            if pi:
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/signin/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            forms = BlogPostForm(request.POST, request.FILES, label_suffix=' ')
            if forms.is_valid():
                title = forms.cleaned_data['title']
                content = forms.cleaned_data['content']
                photo = forms.cleaned_data['photo']
                author = forms.cleaned_data['author']
                reg = BlogPost(title=title, content=content, photo=photo, author=author)
                reg.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            forms = BlogPostForm(label_suffix=' ')
        context = {
            'forms': forms,
        }
        return render(request, 'blog/addnewpost.html', context)
    else:
        return HttpResponseRedirect('/signin/')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = Signup(request.POST)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/signin/')
        else:
            forms = Signup()
        context = {
            'forms': forms,
        }
        return render(request, 'blog/signup.html', context)
    else:
        return HttpResponseRedirect('/login/')


def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = SignInForm(request=request, data=request.POST)
            if forms.is_valid():
                uname = forms.cleaned_data['username']
                upass = forms.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
        else:
            forms = SignInForm(request=request)
        context = {
            'forms': forms,
        }
        return render(request, 'blog/signin.html', context)
    else:
        return HttpResponseRedirect('/')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/signin/')
    else:
        return HttpResponseRedirect('/')


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = PasswordChangeForm(user=request.user, data=request.POST, label_suffix=' ')
            if forms.is_valid():
                forms.save()
                update_session_auth_hash(request, forms.user)
                return HttpResponseRedirect('/signin/')
        else:
            forms = PasswordChangeForm(user=request.user, label_suffix=' ')
        context = {
            'forms': forms,
        }
        return render(request, 'blog/changepassword.html', context)
    else:
        return HttpResponseRedirect('/signin/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = EditProfile(instance=request.user, data=request.POST, label_suffix=' ')
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/')
        else:
            forms = EditProfile(instance=request.user, label_suffix=' ')
        context = {
            'forms': forms,
        }
        return render(request, 'blog/profile.html', context)
    else:
        return HttpResponseRedirect('/signin/')

from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from blog import models
from .forms import *

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/signup.html'

def ProfileView(request):
    post_list =  models.Post.objects.all()
    user_posts=[]
    form = ProfilePicForm
    for post in post_list:
        print(post.member.all())
        for member in post.member.all():
            if request.user==member.user:
                print(post)
                user_posts.append(post)
    context={
        'form':form,
        'post_list':user_posts,
    }
    return render(request, 'accounts/profile.html',context=context)

def ProfileViewOther(request,username):
    user = get_object_or_404(models.User, username=username)
    post_list =  models.Post.objects.all()
    user_posts=[]
    for post in post_list:
        print(post.member.all())
        for member in post.member.all():
            if user==member.user:
                print(post)
                user_posts.append(post)
    context={
        'user_other':user,
        'post_list':user_posts,
    }
    return render(request, 'accounts/profile_other.html',context=context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from GeeksNegar import settings
from django.views import generic

def index(request):
    post_list =  models.Post.objects.order_by('-pub_date')
    context={'post_list' : post_list
    }
    return render(request, 'blog/index.html',context=context)

def post_detail(request,post_id='1'):
    post_like_handle(request,post_id)
    obj = get_object_or_404(models.Post, pk=post_id)
    post_like, created = models.Like.objects.get_or_create(post=obj)
    context={'post' : obj,    
            'post_like' : post_like
    }
    return render(request, 'blog/post_detail.html',context=context)

def post_like_handle(request,post_id='1'):
    if request.method == 'POST':
        user = request.user
        create_id = get_object_or_404(models.Post, id=post_id)
        liked, created = models.Like.objects.get_or_create(post=create_id)
        try:
            user_liked = models.Like.objects.get(post=create_id, user=user)
        except:
            user_liked = None

        if user_liked:
            user_liked.likecount -= 1
            liked.user.remove(request.user)
            user_liked.save()
        else:
            liked.user.add(request.user)
            liked.likecount += 1
            liked.save()
        context={'post' : create_id
        }
        return render(request, 'blog/post_detail.html',context=context)


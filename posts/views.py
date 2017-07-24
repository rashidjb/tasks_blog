from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_create(request):
	context={
	"title": "Create",

	}
	return render(request, 'post_create.html', context)

def post_list(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "List",
    "user": request.user
    }
    return render(request, 'post_list.html', context)

def post_detail(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Detail",
    "instance": instance
    }
    return render(request, 'post_detail.html', context)

def post_update(request):
	context={
	"title": "Update",
	
	}
	return render(request, 'post_update.html', context)

def post_delete(request):
	context={
	"title": "Delete",
	
	}
	return render(request, 'post_delete.html', context)
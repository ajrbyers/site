from django.shortcuts import render, get_object_or_404, redirect

from website import models

def index(request):

	posts = models.Post.objects.filter(is_page=False, is_published=True).order_by('-posted')

	template = 'website/index.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)
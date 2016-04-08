from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

#https://docs.djangoproject.com/en/1.8/topics/http/views/
def post_list(request):
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


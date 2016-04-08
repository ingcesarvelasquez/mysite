from django.shortcuts import render

#https://docs.djangoproject.com/en/1.8/topics/http/views/
def post_list(request):
	return render(request, 'blog/post_list.html', {})

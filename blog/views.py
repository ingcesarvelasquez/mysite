from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from .forms import PostForm
#Mi primera vista basada en clases
from django.views.generic import TemplateView, ListView

class index(TemplateView):
    template_name = 'blog/1vistaGenericaBasadaEnClases.html'
#Fin

class ListarPost(ListView):
    template_name = 'blog/genericListarPost.html'
    model = Post
    context_object_name = 'listaPosts'

#https://docs.djangoproject.com/en/1.8/topics/http/views/
def post_list(request):
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})



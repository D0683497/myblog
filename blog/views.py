from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_create(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_text = request.POST.get('text')
        new_post = Post(title=new_title, text=new_text)
        new_post.save()
        new_post.publish()
        return redirect('post_list')
    return render(request, 'blog/post_create.html', {})

def course_additional(request):
    return render(request, 'course_additional.html', {})
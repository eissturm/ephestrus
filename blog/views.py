from ephestrus.blog.models import Post
from django.template import Context, loader
from django.shortcuts import render_to_response

def home(request):
    post_list = Post.objects.all()
    return render_to_response(
        'blog/list.html',
        {'object_list': post_list}
    )
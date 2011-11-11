from django.shortcuts import render_to_response
from blog.models import Post

def home(request):
    """
    Will find the latest blog post and the latest portfolio entry and pass those into the 'static/home.html' template.
    Blog post will be passed as the 'blog' object, while the portfolio entry will be 'port'.
    """
    blog = Post.objects.filter(published=True)[0]
    return render_to_response(
        'static/home.html',
        {'blog': blog}
    )
    
def search(request):
    pass
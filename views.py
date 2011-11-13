from django.shortcuts import render_to_response
from blog.models import Post
from django.db.models import Q
from django.core.context_processors import csrf

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from forms import ContactForm

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
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(entry__icontains=query)
        )
        results = Post.objects.filter(qset, published="true").distinct()
    else:
        results = []
        
    return render_to_response('static/search.html', {
        "results": results,
        "query": query
    })
    
def contact(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['andrew@ephestr.us']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('static/contact.html', {'form': form},  context_instance=RequestContext(request))
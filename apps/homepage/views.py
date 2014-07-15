from django.shortcuts import render_to_response
from apps.data.models import *
from django.template import RequestContext
from apps.homepage.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail


def index(request):
    entrieslist = Entry.objects.published_entries()
    paginator = Paginator(entrieslist, 3)
    pageno = request.GET.get('page')
    try:
        entries = paginator.page(pageno)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    send_data = {'entries': entries}
    return render_to_response('homepage/index.html',send_data,context_instance=RequestContext(request))

def about(request):
    return render_to_response('homepage/about.html',context_instance=RequestContext(request))

def contact(request):
    success = False
    email = ''
    phone = ''
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            send_mail(message,message,'dilu.seven@gmail.com',[email])
    else:
        form = ContactForm()
    send_data = {'form':form,'success':success,'email':email,'phone':phone,'message':message}
    return render_to_response('homepage/contact.html',send_data,context_instance=RequestContext(request))

@login_required
def profile(request):
    send_data = {}
    return render_to_response('homepage/profile.html',send_data,context_instance=RequestContext(request))

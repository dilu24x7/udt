from django.shortcuts import render_to_response
from apps.data.models import *
from django.template import RequestContext
from apps.homepage.forms import ContactForm

from django.core.mail import send_mail


def index(request):
    print "im er"
    entries = Entry.objects.published_entries()
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

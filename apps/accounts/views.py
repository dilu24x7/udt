# Create your views here.
from django.shortcuts import render_to_response,redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from apps.accounts.forms import RegisterForm
from django.contrib.auth.views import login



@login_required
def profile(request):
    send_data = {'profile':request.user.get_profile()}
    print send_data
    return render_to_response('accounts/profile.html',send_data,context_instance=RequestContext(request))

def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(request,user)
        return redirect(reverse('accounts_profile'))

    send_data = {'form':form}
    return render_to_response('accounts/register.html',send_data,context_instance=RequestContext(request))

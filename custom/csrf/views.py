from django.shortcuts import render_to_response

def csrf_rejected(request,reason=''):
    send_data = {'reason': reason}
    render_to_response('csrf/rejected.html',send_data)

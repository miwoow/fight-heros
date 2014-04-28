from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    return render_to_response('ui/index.html', {}, context_instance=RequestContext(request))

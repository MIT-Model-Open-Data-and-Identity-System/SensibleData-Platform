from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

from accounts import manager
from utils import platform_config
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def home(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))


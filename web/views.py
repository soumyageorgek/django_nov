# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def comment(request):
    if request.method == 'GET':
    	return render_to_response('comment.html',{})
        
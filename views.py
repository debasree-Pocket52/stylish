# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


from django.template import loader

# Create your views here.


def Index(request):
	template = loader.get_template("login.html")
	context = {"a":"b"}
	return HttpResponse(template.render(context, request))
	#return HttpResponse("My first django app...")


#def DebaSree(request):
#	return HttpResponse("Going to cakewala...")
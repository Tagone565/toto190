from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Mypics
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    all_pic = Mypics.objects.all()
    template = loader.get_template('v.html')
    context = {'all_pic': all_pic }
    return HttpResponse(template.render(context, request))

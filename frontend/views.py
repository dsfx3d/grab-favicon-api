from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from grabicon import FaviconGrabber

from .forms import GrabFaviconForm



class IndexView(View):

    def get(self, request):
        context = dict(form=GrabFaviconForm())
        return render(request, 'index.html', context)

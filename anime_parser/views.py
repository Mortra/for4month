from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import  reverse
from django.views.generic import ListView

from . import models,forms
import requests

from .models import Anime


class ParserFormView(generic.FormView):
    template_name = 'pyparser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('anime/')
        else:
            return super(ParserFormView,self).post(request,*args,**kwargs)




class AnimeViews(ListView):
    model = Anime
    template_name = 'anime.html'

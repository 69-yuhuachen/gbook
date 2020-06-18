from django.shortcuts import render
from django.views.generic import *
from django.urls import reserve_lazy
from .models import Message
from django.contrib.auth.mixin import LoginRequireMixin

# Create your views here.
#留言列表
class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    MODEL = Message

class MessageCreate(CreatView):
    model = Message   
    fields = ['user','subject','content']
    success_url = reverese_lazy('msg_list')
class MessageDelete( LoginRequireMixin, DeleteView):
    model = Message   
    fields = ['user','subject','content']
    success_url = reverese_lazy('msg_list')
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Carpa
from .serializers import CarpaSerializer
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache  import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm





class CarpaList(generics.ListCreateAPIView):
    queryset =Carpa.objects.all()
    serializer_class = CarpaSerializer


class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:carpa_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
        #aca tendria que ir el token
        token = True #esto hay que cambiarlo
        if token:
            login(self.request,form.get_user())
            return super(Login,self).form_valid(form)



class TestRequest(APIView):
    def get(self, request):
        return Response({
            "test": "data"
        })



from dataclasses import fields
from multiprocessing import Value, context
from sre_constants import SUCCESS
from django.shortcuts import render
from .models import Newspaper
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


#from first_app.forms import NewspaperForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect


from django.views.generic.edit import CreateView #

from first_app.forms import CustomUserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
import re
from django.template import loader
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.template import Context
from django.http import HttpResponse
from datetime import date, datetime



"""
#django form use-->

class IndexPageView(FormView): 
    model = Newspaper
    template_name = 'index.html'
    form_class =NewspaperForm
    success_url = 'index'
    def form_valid(self, form):
        
        obj=Newspaper(title=form.cleaned_data['title'],author_name=form.cleaned_data['author_name'],content=form.cleaned_data['content'],image=form.cleaned_data['image'])
        obj.save()
        
        return super().form_valid(form)
"""
class FormPageView(TemplateView): 
    model = Newspaper
    template_name = 'form.html'
   # form_class =NewsPaperForm
    #success_url = 'form'
    def post(self,request,*args,**kwargs):
       
        if request.POST['name'] !='':
            
           
            propic = Newspaper(title=request.POST['name'] , author_name =self.request.user, content =request.POST['content'],image=request .FILES['image'])
            propic.save()
            return redirect('form')
        
              
            
            
class SignupPageView(TemplateView) :
    model=Newspaper
    template_name='signup.html'
   
    
    def post(self,request):
        if request.method == 'POST':
            #return redirect('login')
            name = request.POST['username']
            email = request.POST['email']
            password = request.POST["password1"]
            confirmation = request.POST["password2"]
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            
            if re.search(regex, email):
                pass
            else:
                messages.error(request, 'invalid email')
                return redirect('signup')
               
            if password != confirmation:
                messages.error(request, 'password dose not match')
                return redirect('signup')
               
            already = User.objects.filter(email=email)
            if bool(already):
                messages.error(request, 'email already registered')
                return redirect('signup')
                
            user = User.objects.create_user(
                username=name,
                email=email,
            
                password=password,
                )
            user.save()
            
            return redirect('login')
            
        
        
    
class LoginPageView(TemplateView) :
   # model=Newspaper
    template_name='login.html'
    def post(self,request):
        #print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate( username=email, password=password)
       
    
        if user is not None:
            
            login(request, user)
            return redirect('home')
            
        
        else:
            messages.error(request, 'if you have no account, please! sign up')
            return redirect('login')
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'successfully loggoed out')
        return redirect('home')        
        
        
        
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class HomePageView(ListView):
    
    #template_name='home.html' 


#class NewspaperListView(ListView):
    model=Newspaper
    context_object_name="papers"
    template_name='home.html' 
    def get_queryset(self):
        return Newspaper.objects.filter(published_date__lte = datetime.now()).order_by("-published_date") 
    
    
    
class NewspaperDetailsView(DetailView):
    model=Newspaper
    template_name='newspaper_details.html' 
    context_object_name='newspaper'
    
class NewspaperUpdateView(TemplateView):
    model=Newspaper
    template_name='newspaper_update_form.html'
    
    def post(self,request,*args,**kwargs):
           
        obj=Newspaper.objects.get(pk=self.kwargs['pk'])
        obj.title=self.request.POST['name']
        obj.content=self.request.POST['content']
        obj.image=self.request.FILES['image']
        obj.save()
        return redirect('home')
    
    def get_context_data(self, **kwargs):
        
        obj=Newspaper.objects.get(pk=self.kwargs['pk'])
        context = {
            'titlename': obj.title,
            'content': obj.content,
            'image': obj.image,
            
        }

       
        return context
    
    
class NewspaperDeleteView(DeleteView):
    model = Newspaper
    template_name='newspaper_delete.html'
    success_url = reverse_lazy('home')
     
    def test_func(self):  # new
        obj = self.get_object()
        return obj.author_name == self.request.user    
    
    
            
           
            
    
    
    
    
    
    
        
    
    
      
         
    
       
    











   
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.views import View
from .forms import MyUserCreationForm
# Create your views here.

class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/library')
        form = MyUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    def post(self,request):
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/library')
        return render(request, 'registration/signup.html', {'form': form})
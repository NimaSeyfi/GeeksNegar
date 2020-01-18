from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/signup.html'

def ProfileView(request):
    context={
    }
    return render(request, 'accounts/profile.html',context=context)
from django import forms
from django.contrib.auth.models import User
from Account.models import UserProfile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        
        model = UserProfile
        fields = ['user_picture',]



class UserUpdateForm(UpdateView):
    
    model = UserProfile
    fields = ['first_name','last_name' ,'birth_date', 'user_picture']
    template_name = 'accounts/user_form.html'
    
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.get_object().username})

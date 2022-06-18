from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from .models import NeighbourHood, Profile, Business, Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','email','phone_no']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','info'] 
        
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image','health_center','health_email','health_contact']         
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['image','name','email','phone_no']            
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')

def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'profile-update.html', {'form': form})


def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})






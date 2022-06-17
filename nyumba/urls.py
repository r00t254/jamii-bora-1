from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('profile-update/',views.update_profile, name='update_profile'),
    path('profile/<pk>',views.profile, name = 'profile'),
    path('create-hood/',views.createhood, name='createhood'), 
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]


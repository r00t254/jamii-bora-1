from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User,on_delete = models.CASCADE,related_name='administration',null=True)
    description = models.CharField(max_length=250)
    occupants = models.IntegerField(default=0, null=True, blank=True)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

    def create_neighborhood(self):
        """
        A method that creates a neighbourhood
        """
        self.save()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        """
        A method that finds a neighbourhood using its id
        """
        return cls.objects.filter(id=neighborhood_id) 



    @classmethod
    def update_neighbourhood(cls, id):
        """
        A method that updates a neighbourhood
        """
        neighbourhood = cls.objects.filter(id=id).update(id=id)
        return neighbourhood   

    def delete_neighborhood(self):
        """
        A method that deletes a neighbourhood
        """
        self.delete() 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_no = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user    

class Business(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)     
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE, related_name='business',null=True)
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name      

    def create_business(self):
        """
        A method that creates a business
        """
        self.save()


    @classmethod
    def search_business(cls,search_term):
        """
        A method that searches a business
        """          
        businesses = cls.objects.filter(name__icontains = search_term).all()
        return businesses 

    @classmethod
    def find_business(cls, business_id):
        """
        A method that finds a business using its id
        """         
        business = Business.objects.filter(id=business_id)
        return business  

    @classmethod
    def update_business(cls, id):
        """
        A method that updates a business using its id
        """  
        business = cls.objects.filter(id=id).update(id=id)
        return business

    def delete_business(self):
        """
        A method that deletes a business
        """        
        self.delete()


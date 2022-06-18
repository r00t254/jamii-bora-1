from django.test import TestCase

# Create your tests here.from django.test import TestCase
from .models import Profile,Business,NeighbourHood

class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
    

        self.test_business = Business.objects.create(name='Spashop',image='example.jpg',user='sareto',email='example@gmail.com',phone_number='0712345678',neighbourhood='kitengela')

        self.test_business.save()

    def test_save_method(self):
        self.test_business.save()
        test_business = Business.objects.all()
        self.assertTrue(len(test_business) > 0)


    def test_delete_method(self):
        self.Business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)   

    def tearDown(self):
        Business.objects.all().delete() 


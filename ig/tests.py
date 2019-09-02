from django.test import TestCase
import datetime as dt
from .models import Profile,Image,Comment
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    test for profile
    '''
    # Set up method
    def setUp(self):
        self.John= Profile(profile_photo = 'Nairobi',bio ='', user_id = 1)
    def test_instance(self):
        self.assertTrue(isinstance(self.John,Profile))

    def test_save_method(self):
        self.John.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.John.delete_profile
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


class ImageTestClass(TestCase):
    '''
    test for image
    '''
    # Set up method
    def setUp(self):
        self.Nairobi= Image(photo='js_3kcls7r.jpg',image_name='rio',image_caption='animation',post_date='2019-07-27 11:30:33.999607+03',likes='t',profile =User.id)
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Image))

    def test_save_method(self):
        self.Nairobi.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.Nairobi.delete_image
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

def tearDown(self):
       Profile.objects.all().delete()
       Comment.objects.all().delete()
       Image.objects.all().delete()

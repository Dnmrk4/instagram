from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profilepics')
    bio = models.CharField(max_length=2000)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    class Meta:
        ordering = ('user',)

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
        
    @classmethod
    def search_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains = search_term)
        return profile


    def __str__(self):
        return self.bio

class Image(models.Model):
    photo = models.ImageField(upload_to='photos')
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=2000)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('post_date',)

    def delete_image(self):
        self.delete()       

    def save_image(self):
        self.save()

    @classmethod
    def get_allImages(cls):
        images = cls.objects.all()
        return images
    

    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images
        
    def __str__(self):
        return self.image_name

class Comment(models.Model):
    comment = models.CharField(max_length=50)
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('posted_on',)

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comment.objects.filter(image__pk = id)
        return comments

    def __str__(self):
        return self.comment

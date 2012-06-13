from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profilePicture = models.ImageField(upload_to='profilePictures')
    slug = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


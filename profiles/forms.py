from django.forms import ModelForm
from models import UserProfile 
from models import User
from django.template.loader import *

class UserProfileForm(ModelForm):    
    class Meta:
        model = UserProfile
        fields = ('profilePicture', 'firstName', 'lastName','slug' )
#    def as_p(self):
#         return render_to_string('forms/form.html')
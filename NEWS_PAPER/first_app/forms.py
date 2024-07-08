from django.forms import ModelForm
from first_app.models import Newspaper

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
























"""
class NewspaperForm(ModelForm):
    class Meta:
        model = Newspaper
        fields= "__all__"
"""        
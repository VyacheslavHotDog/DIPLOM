from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(CustomUser):
        model = CustomUser
        # fields = '__all__'
        fields = ('username', 'first_name', 'last_name', 'age', 'gender', 'country', 'email', 'city',
                  'about', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


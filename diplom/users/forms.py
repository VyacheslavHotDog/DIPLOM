from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(CustomUser):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


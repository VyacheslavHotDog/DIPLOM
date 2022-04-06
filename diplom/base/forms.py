from django import forms
from .models import Trip


class AddTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['header', 'description', 'dateBegin', 'dateEnd', 'country', 'category', 'logo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control pb-0'

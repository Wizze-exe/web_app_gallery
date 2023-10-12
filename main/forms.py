from .models import Arts
from django.forms import ModelForm


class ArtForm(ModelForm):
    class Meta:
        model = Arts
        fields = ['title', 'description', 'price', 'art']

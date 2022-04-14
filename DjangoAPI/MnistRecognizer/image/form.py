from django import forms
from .models import Image, BoxForm

class ImageForm(forms.ModelForm):
    image = forms.ImageField(required = True, label = '',
    widget=forms.FileInput(
        attrs={'id':'upload_image'}
    )
    )
    class Meta:
        model = Image
        fields = ('image',)

class BoxForm(forms.ModelForm):
    box_check = forms.BooleanField(required=False, label = 'Check this box if your image is type 2')
    class Meta:
        model = BoxForm
        fields = ('box_check',)

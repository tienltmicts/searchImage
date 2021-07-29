from django import forms

class ImageForms(forms.Form):

    id_selfie = forms.ImageField()
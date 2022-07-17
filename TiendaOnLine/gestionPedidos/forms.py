from django import forms


class contactoforms(forms.Form):
    
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea)
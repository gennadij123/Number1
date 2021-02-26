from django import forms

class FullUrlForm(forms.Form):
    url=forms.URLField(label='Enter your URL',max_length=100)

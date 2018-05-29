#contact/forms.py

from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=50)
    message = forms.CharField(widget=forms.Textarea, required=True)

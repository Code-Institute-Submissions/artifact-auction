from django import forms

"""
A form to take contact details and query from user
"""
class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    subject = forms.CharField(label='Subject', required=True)
    enquiry = forms.CharField(widget=forms.Textarea(attrs={
              "style" : "resize: None; width:100%; border:None; outline: None"
              }))
    email_address = forms.EmailField(required=True)

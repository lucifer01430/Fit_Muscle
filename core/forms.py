from django import forms
import re
from .models import Subscription  

class AppointmentForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={
            'required': 'Full name is required.',
            'max_length': 'Full name cannot exceed 100 characters.'
        }
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        error_messages={
            'required': 'Phone number is required.',
            'max_length': 'Phone number cannot exceed 15 characters.'
        }
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Email address is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=False,
        max_length=500,
        error_messages={
            'max_length': 'Message cannot exceed 500 characters.'
        }
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Validate phone number format (e.g., 10 digits or with country code)
        if not re.match(r'^\+?\d{10,15}$', phone_number):
            raise forms.ValidationError('Please enter a valid phone number (10-15 digits, optionally starting with +).')
        return phone_number

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not re.match(r'^[a-zA-Z\s]+$', full_name):
            raise forms.ValidationError('Full name can only contain letters and spaces.')
        return full_name

class SubscriptionForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Email address is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if email already exists in Subscription model
        if Subscription.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already subscribed.')
        return email

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Name is required.'})
    email = forms.EmailField(required=True, error_messages={'required': 'Email is required.', 'invalid': 'Please enter a valid email address.'})
    website = forms.URLField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=True, error_messages={'required': 'Comment is required.'})
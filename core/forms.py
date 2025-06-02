from django import forms
import re
from .models import Subscription, Comment


# ----------------------
# Appointment Form
# ----------------------
class AppointmentForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'inputt-text'}),
        error_messages={
            'required': 'Full name is required.',
            'max_length': 'Full name cannot exceed 100 characters.'
        }
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'inputt-text'}),
        error_messages={
            'required': 'Phone number is required.',
            'max_length': 'Phone number cannot exceed 15 characters.'
        }
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'inputt-text'}),
        error_messages={
            'required': 'Email address is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )
    message = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={'placeholder': 'Message...', 'class': 'inputt-text'}),
        error_messages={
            'max_length': 'Message cannot exceed 500 characters.'
        }
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise forms.ValidationError('Enter a valid phone number (10–15 digits).')
        return phone

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise forms.ValidationError('Full name can only contain letters and spaces.')
        return name


# ----------------------
# Subscription Form
# ----------------------
class SubscriptionForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'subscribe-control'}),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.'
        }
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscription.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already subscribed.')
        return email


# ----------------------
# Blog Comment Form (ModelForm)
# ----------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']  # include name/email now
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Your Name',
                'class': 'comment-form-control w-100 border-0 shadow-none',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Your Email',
                'class': 'comment-form-control w-100 border-0 shadow-none',
            }),
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'class': 'comment-form-control w-100 border-0 shadow-none',
            }),
        }
        error_messages = {
            'name': {'required': 'Name is required.'},
            'email': {'required': 'Email is required.'},
            'comment': {'required': 'Comment is required.'},
        }
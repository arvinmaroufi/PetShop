from django import forms
from .models import ContactUs
from django.forms import ValidationError


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'subject', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) > 200:
            raise ValidationError("تعداد کارکتر وارد شده بیش از حد مجاز می باشد")
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) > 100:
            raise ValidationError("تعداد کارکتر وارد شده بیش از حد مجاز می باشد")
        return subject


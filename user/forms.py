from django import forms

from .models import BaseUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = BaseUser
        fields = ("email",)

    def clean_email(self):
        """
        Clean the email field and perform validation checks.
        Raises a ValidationError if the email is not valid.
        Returns the cleaned email value.
        """
        email = self.cleaned_data.get("email")
        if email and BaseUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_password2(self):
        """
        Clean the password2 field and perform validation checks.
        Raises a ValidationError if the password is less than 8 characters long
        or if password2 does not match password.
        Returns the cleaned password2 value.
        """
        cd = self.cleaned_data

        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

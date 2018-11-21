from django                     import forms
from django.contrib.auth.models import User
from django.core                import validators
from main_app.models             import UserProfileInfo
from django.utils.translation import gettext as _


class UserForm(forms.ModelForm):
    #username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control',}))
    email   =  forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control',}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control',}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control ',}))

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            msg = "Passwords are not the same"
            self.add_error('password', msg)


    class Meta():
        model = User
        fields = ('username','email','password','confirm_password')
        labels = {
            'username': _('Username:'),
            'email': _('Email:'),
            'password':  _('Password:'),
            'confirm_password':    _('Repeat Password:'),
        }
        help_texts = {
            'username': _('Minimum length 6 characters'),

        }

        error_messages = {
            'username': {
                'required': _("REQUIRED")
            },
            'password': {
                'required': _("REQUIRED")
            },
            'confirm_password': {
                'required': _("REQUIRED")
            },
            'email': {
                'required': _("REQUIRED")
            },
        }
        widgets = {
                    'username':  forms.TextInput(attrs={'class':'form-control',}),
                }


class UserProfileForm(forms.ModelForm):

    nick        = forms.CharField(required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ('nick','profile_pic')
        exclude = ('user',)

from django                     import forms
from django.contrib.auth.models import User
from django.core                import validators
from main_app.models             import UserProfileInfo
from django.utils.translation import gettext as _



class UserForm(forms.ModelForm):
    """ Clase formulario para datos de usuarios basicos"""
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control',}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control ',}))

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            msg = "Las contraseñas no coinciden"
            self.add_error('password', msg)

    class Meta():
        model = User
        msg_required= "Campo obligatorio"
        fields = ('username','email','password','confirm_password')
        labels = {
            'username': _('Nombre de usuario:'),
            'email': _('Email:'),
            'password':  _('Contraseña:'),
            'confirm_password':    _('Repita contraseña:'),
        }
        help_texts = {
            'username': _('longitud mínima 6 cáracteres'),
        }
        error_messages = {
            'username': {
                'max_length': _("Longitud no válida"),
                'required': _(msg_required)
            },
            'password': {
                'required': _(msg_required)
            },
            'confirm_password': {
                'required': _(msg_required)
            },
            'email': {
                'required': _(msg_required)
            },
        }
        widgets = {
                    'username':  forms.TextInput(attrs={'class':'form-control',}),
                    'email':forms.EmailInput(attrs={'class':'form-control',}),

                }
class UserProfileForm(forms.ModelForm):
    """ Clase formulario detalles adicionales sobre el usuario"""
    user_info= forms.CharField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ('user_info',)
        exclude = ('user',)
        widgets = {
                    'username':  forms.TextInput(attrs={'class':'form-control',}),
                    'email':forms.EmailInput(attrs={'class':'form-control',}),
                    'password': forms.PasswordInput(attrs={'class':'form-control',}),
                    'confirm_password':  forms.PasswordInput(attrs={'class':'form-control',}),
                }
        help_texts = {
            'user_info': _('(No necesario)'),
        }

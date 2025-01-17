from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from user_mgmt_app.models import UserProfileInfo,FriendRelationship
from django.core.files.images import get_image_dimensions


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
        msg_required = "Campo obligatorio"
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'confirm_password'
        )

        fields_required= (
            'username',
            'email',
            'password',
            'confirm_password'
            )

        labels = {
            'username': _('Nombre de usuario :'),
            'first_name': _('Nombre :'),
            'last_name': _('Apellidos :'),
            'email': _('Email:'),
            'password':  _('Contraseña :'),
            'confirm_password':    _('Repita contraseña :'),
        }
        help_texts = {
            'username': _('longitud mínima 6 cáracteres'),
            'first_name': _('No es obligatorio'),
            'last_name': _('No es obligatorio'),
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
                    'first_name':  forms.TextInput(attrs={'class':'form-control',}),
                    'last_name':  forms.TextInput(attrs={'class':'form-control',}),
                    'email':forms.EmailInput(attrs={'class':'form-control',}),

                }
class UserProfileForm(forms.ModelForm):
    """ Clase formulario detalles adicionales sobre el usuario"""


    class Meta():
        model = UserProfileInfo
        fields = ('user_info','profile_pic')
        exclude = ('user','friends')
        labels = {
                'user_info': _('Información sobre el usuario :'),
                'profile_pic': _('Imagen de perfil:'),

                }
        help_texts = {
            'user_info': _('(Información relevante sobre el usuario.No necesario)'),
        }
        widgets = {
                    'user_info': forms.Textarea(attrs={'class':'form-control input-lg description-TextInput',}),
        }

class FriendForm(forms.Form):
    friend = forms.CharField(label='Nombre de usuario:', widget=forms.TextInput(attrs={'required':'required','class':'form-control',}))
    def clean(self):
        all_clean_data = super( FriendForm,self).clean()
        friend    = all_clean_data['friend']

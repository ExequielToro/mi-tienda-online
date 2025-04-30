from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoMedico
        fields = ['p_img']
        
class CustomUserCreationForm(UserCreationForm):
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = User.objects.filter(username__iexact=nombre).exists()
      
        if existe:
            raise ValidationError("Nombre ya existe")

        return nombre  # Retorna el valor validado después de la validación

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.ModelForm):
       
   aviso = forms.BooleanField(required=True)
   class Meta:
         model = Contacto
         fields = '__all__'
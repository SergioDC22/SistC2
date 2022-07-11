from dataclasses import field
from django import forms
from .models import Cliente
from django.core import validators


class ClienteForm(forms.ModelForm):

    CUIT = forms.CharField(
        validators=[
            validators.MinLengthValidator(11, "El cuit es demasiado corto"),
            validators.MaxLengthValidator(11, "El cuit es demasiado largo"),
            validators.RegexValidator(
                '^[0-9]*$', "El cuit esta mal formado, solo se admiten numeros")
        ])


    RazonSocial = forms.CharField(

        validators=[
            validators.MinLengthValidator(
                5, "La razon social es demasiada corta"),
            validators.MaxLengthValidator(
                50, "La razon social es demasiada largo")
        ])

    class Meta:
        model = Cliente
        fields = '__all__'

    def clean__CUIT(self):
        cuit = self.changed_data['CUIT']
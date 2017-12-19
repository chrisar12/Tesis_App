from django import forms
from .models import SituacionSalud


class SituacionSaludForm(forms.ModelForm):

    class Meta:
        model = SituacionSalud
        # fields ='__all__'
        fields = [
            'edad',
            'sexo',
            'distrito',
            'cie',
            'seguro',
            'niveleconomico',
            'zona',
            'eess'
        ]

        widgets = {
            'edad': forms.NumberInput(),
            'sexo': forms.Select(),
            'distrito': forms.Select(),
            'cie': forms.Select(),
            'seguro': forms.Select(),
            'niveleconomico': forms.Select(),
            'zona': forms.Select(),
            'eess': forms.Select()
        }

#  Asi pones estilos o clases a los imputs
#   widgets = {
#         'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
#                                              'placeholder': 'Ingrese una descripcion'}),
#         'delitos': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
#     }

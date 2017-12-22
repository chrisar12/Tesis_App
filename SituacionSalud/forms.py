from django import forms
from .models import *


class SituacionSaludForm(forms.ModelForm):
    class Meta:
        model = SituacionSalud
        # fields ='__all__'
        fields = [
            'sexo',
            'distrito',
            'cie',
            'seguro',
            'niveleconomico',
            'zona',
            'eess'
        ]

        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-control '}),
            'distrito': forms.Select(attrs={'class': 'form-control '}),
            'cie': forms.Select(attrs={'class': 'form-control '}),
            'seguro': forms.Select(attrs={'class': 'form-control '}),
            'niveleconomico': forms.Select(attrs={'class': 'form-control '}),
            'zona': forms.Select(attrs={'class': 'form-control '}),
            'eess': forms.Select(attrs={'class': 'form-control '})
        }

#  widgets = {
#       'distrito': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
#                                            'placeholder': 'Ingrese una descripcion'}),
#      'edad': forms.SelectMultiple(attrs={'class': 'form-control select2'})
# }


class FactoresCondicionantesForm(forms.ModelForm):
    class Meta:
        model = Poblacion
        # fields ='__all__'

        fields = [
            'anio',
            'pobtotal',
            'pobmujer',
            'pobvaron',
            'nacimiento',
            'muerte',
            'rangoedad'
        ]

        widgets = {
            'anio': forms.IntegerField(required=False),
            'pobtotal': forms.IntegerField(),
            'pobmujer': forms.IntegerField(),
            'pobvaron': forms.IntegerField(),
            'nacimiento': forms.IntegerField(),
            'muerte': forms.IntegerField()

        }
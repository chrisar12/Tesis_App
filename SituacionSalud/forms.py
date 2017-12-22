from django import forms
from .models import SituacionSalud


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

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
            'edad': forms.NumberInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control select2'}),
            'distrito': forms.Select(),
            'cie': forms.Select(),
            'seguro': forms.Select(),
            'niveleconomico': forms.Select(),
            'zona': forms.Select(),
            'eess': forms.Select()
        }


#  widgets = {
 #       'distrito': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
  #                                            'placeholder': 'Ingrese una descripcion'}),
   #      'edad': forms.SelectMultiple(attrs={'class': 'form-control select2'})
    # }

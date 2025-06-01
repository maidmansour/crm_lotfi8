from django import forms
from django.forms import ModelForm
from .models import Proprietaire


class ProprietaireForm(ModelForm):
    class Meta:
        model = Proprietaire
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProprietaireForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
        
        self.fields['type_proprietaire'].widget.attrs['class'] = "form-select form-select-sm"
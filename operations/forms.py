from django import forms
from .models import Operation
from proprietes.models import Propriete
from clients.models import Client
from proprietaires.models import Proprietaire

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(OperationForm, self).__init__(*args, **kwargs)
        self.fields.update({
                'propriete' : forms.ModelChoiceField(queryset=Propriete.objects.all(), required=True),
                'proprietaire' : forms.ModelChoiceField(queryset=Proprietaire.objects.all(), required=True),
                'client' : forms.ModelChoiceField(queryset=Client.objects.all(), required=True),
                
            })
        self.fields['date_operation'].widget=forms.widgets.DateInput(attrs={'type': 'date'})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control'
            
        self.fields['propriete'].widget.attrs['class'] = 'mb-2 form-select  form-select-sm'
        self.fields['proprietaire'].widget.attrs['class'] = 'mb-2 form-select  form-select-sm'
        self.fields['client'].widget.attrs['class'] = 'mb-2 form-select  form-select-sm'
        self.fields['type_operation'].widget.attrs['class'] = 'mb-2 form-select  form-select-sm'
from django import forms
from django.core.exceptions import ValidationError
from .models import Secteur, Residence, Typebien, Soustypebien, Agent, Intermidiaire, Quartier

class SecteurForm(forms.ModelForm):
    class Meta:
        model = Secteur
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(SecteurForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'
    
    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        qs = Secteur.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Ce Champs est déjà pris.")
        return self.cleaned_data['title']
        
class ResisenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ResisenceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'
    
    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        qs = Residence.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Ce Champs est déjà pris.")
        return self.cleaned_data['title']


class TypebienForm(forms.ModelForm):
    class Meta:
        model = Typebien
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(TypebienForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'
    
    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        qs = Typebien.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Ce Champs est déjà pris.")
        return self.cleaned_data['title']

class SoustypebienForm(forms.ModelForm):
    class Meta:
        model = Soustypebien
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(SoustypebienForm, self).__init__(*args, **kwargs)
        self.fields.update({
                'type_bien' : forms.ModelChoiceField(queryset=Typebien.objects.all().order_by('title'), required=True)})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'

        self.fields['type_bien'].widget.attrs['class'] = "form-select form-select-sm"
    
    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        qs = Soustypebien.objects.filter(title__iexact=title, type_bien=self.cleaned_data['type_bien'])
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Ce Champs est déjà pris.")
        return self.cleaned_data['title']

class QuartierForm(forms.ModelForm):
    class Meta:
        model = Quartier
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(QuartierForm, self).__init__(*args, **kwargs)
        self.fields.update({
                'secteur' : forms.ModelChoiceField(queryset=Secteur.objects.all().order_by('title'), required=True)})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'

        self.fields['secteur'].widget.attrs['class'] = "form-select form-select-sm"

    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        qs = Quartier.objects.filter(title__iexact=title, secteur=self.cleaned_data['secteur'])
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Ce Champs est déjà pris.")
        return self.cleaned_data['title']

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'
    
    


class IntermidiaireForm(forms.ModelForm):
    class Meta:
        model = Intermidiaire
        exclude = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(IntermidiaireForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'
    
    
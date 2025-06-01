from django import forms
from django.forms import ClearableFileInput
from .models import Propriete, Intermidiaire, Soustypebien, Typebien, Residence, Secteur, Agent, Quartier
from proprietaires.models import Proprietaire

class RechercheForm(forms.ModelForm):
    price_min = forms.IntegerField(required=False)
    price_max = forms.IntegerField(required=False)
    bedrooms_min = forms.IntegerField(required=False)
    bedrooms_max = forms.IntegerField(required=False)
    class Meta:
        model = Propriete
        fields = ['secteur', 'proprietaire', 'reference', 'residence', 'bedrooms_min', 'bedrooms_max', 'price_min', 'price_max', 'type_bien', 'intermidiaire', 'agent', 'type_operation', 'exclusive']

    def __init__(self, *args, **kwargs):
        super(RechercheForm, self).__init__(*args, **kwargs)
        self.fields.update({
                'proprietaire' : forms.ModelChoiceField(queryset=Proprietaire.objects.all().order_by('nom_raison_sociale'), required=False),
                'intermidiaire' : forms.ModelChoiceField(queryset=Intermidiaire.objects.all().order_by('lastname'), required=False),
                'type_bien' : forms.ModelChoiceField(queryset=Typebien.objects.all().order_by('title'), required=False),
                'residence' : forms.ModelChoiceField(queryset=Residence.objects.all().order_by('title'), required=False),
                'secteur' : forms.ModelChoiceField(queryset=Secteur.objects.all().order_by('title'), required=False),
                'agent' : forms.ModelChoiceField(queryset=Agent.objects.all().order_by('lastname'), required=False),
                
            })
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-select  form-select-sm'   

        self.fields['reference'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['bedrooms_min'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['bedrooms_max'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['price_min'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['price_max'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['exclusive'].widget.attrs['class'] = "form-check-input"
        self.fields['reference'].required =False
        self.fields['type_operation'].required =False
        

class ProprieteForm(forms.ModelForm):
    class Meta:
        model = Propriete
        exclude = ('created_at',)
    
    def __init__(self, *args, **kwargs):
        super(ProprieteForm, self).__init__(*args, **kwargs)
        self.fields.update({
                'proprietaire' : forms.ModelChoiceField(queryset=Proprietaire.objects.all().order_by('nom_raison_sociale'), required=True),
                'intermidiaire' : forms.ModelChoiceField(queryset=Intermidiaire.objects.all().order_by('lastname'), required=False),
                'type_bien' : forms.ModelChoiceField(queryset=Typebien.objects.all().order_by('title'), required=True),
                'sous_type_bien' : forms.ModelChoiceField(queryset=Soustypebien.objects.all().order_by('title'), required=False),
                'residence' : forms.ModelChoiceField(queryset=Residence.objects.all().order_by('title'), required=False),
                'secteur' : forms.ModelChoiceField(queryset=Secteur.objects.all().order_by('title'), required=True),
                'quartier' : forms.ModelChoiceField(queryset=Quartier.objects.all().order_by('title'), required=True),
                'agent' : forms.ModelChoiceField(queryset=Agent.objects.all().order_by('lastname'), required=False),
                
            })
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-2 form-control form-control-sm'
        
        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['columns'] = 8
        self.fields['proprietaire'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['intermidiaire'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['agent'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['quartier'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['type_operation'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['secteur'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['type_bien'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['sous_type_bien'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['residence'].widget.attrs['class'] = "form-select form-select-sm"
        self.fields['occuped_date'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['libre_date'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['block'].widget.attrs['class'] = "form-control form-control-sm"
        self.fields['origine_prospection'].widget.attrs['class'] = "form-check-input"
        self.fields['origine_interne'].widget.attrs['class'] = "form-check-input"
        self.fields['origine_intermidiaire'].widget.attrs['class'] = "form-check-input"
        self.fields['residentiel'].widget.attrs['class'] = "form-check-input"
        self.fields['individuel'].widget.attrs['class'] = "form-check-input"
        self.fields['immeuble'].widget.attrs['class'] = "form-check-input"
        self.fields['habitation'].widget.attrs['class'] = "form-check-input"
        self.fields['commercial'].widget.attrs['class'] = "form-check-input"
        self.fields['mixte'].widget.attrs['class'] = "form-check-input"

        self.fields['recent'].widget.attrs['class'] = "form-check-input"
        self.fields['ancien'].widget.attrs['class'] = "form-check-input"
        self.fields['neuf'].widget.attrs['class'] = "form-check-input"
        self.fields['a_renover'].widget.attrs['class'] = "form-check-input"
        self.fields['semi_fini'].widget.attrs['class'] = "form-check-input"
        self.fields['economique'].widget.attrs['class'] = "form-check-input"
        self.fields['haut_standing'].widget.attrs['class'] = "form-check-input"
        self.fields['my_standing'].widget.attrs['class'] = "form-check-input"

        self.fields['vide'].widget.attrs['class'] = "form-check-input"
        self.fields['semi_meuble'].widget.attrs['class'] = "form-check-input"
        self.fields['meuble'].widget.attrs['class'] = "form-check-input"
        self.fields['equipee'].widget.attrs['class'] = "form-check-input"
        self.fields['semi_equipee'].widget.attrs['class'] = "form-check-input"
        self.fields['collective'].widget.attrs['class'] = "form-check-input"
        self.fields['titree'].widget.attrs['class'] = "form-check-input"

        self.fields['cuisine_equipee'].widget.attrs['class'] = "form-check-input"
        self.fields['cuisine_amenagee'].widget.attrs['class'] = "form-check-input"
        self.fields['cuisine_lesdeux'].widget.attrs['class'] = "form-check-input"
        self.fields['cuisine_buanderie'].widget.attrs['class'] = "form-check-input"

        self.fields['piscine_privee'].widget.attrs['class'] = "form-check-input"
        self.fields['piscine_chauffee_privee'].widget.attrs['class'] = "form-check-input"
        self.fields['jacozzi_privee'].widget.attrs['class'] = "form-check-input"
        self.fields['jardin_privee'].widget.attrs['class'] = "form-check-input"
        self.fields['hammam_beldi_privee'].widget.attrs['class'] = "form-check-input"
        self.fields['piscine_collective'].widget.attrs['class'] = "form-check-input"
        self.fields['piscine_chauffee_collective'].widget.attrs['class'] = "form-check-input"
        self.fields['jacozzi_collective'].widget.attrs['class'] = "form-check-input"
        self.fields['jardin_collective'].widget.attrs['class'] = "form-check-input"
        self.fields['hammam_beldi_collective'].widget.attrs['class'] = "form-check-input"
        self.fields['ascenseur'].widget.attrs['class'] = "form-check-input"
        self.fields['escalier_secour'].widget.attrs['class'] = "form-check-input"
        self.fields['security'].widget.attrs['class'] = "form-check-input"
        self.fields['syndic'].widget.attrs['class'] = "form-check-input"
        self.fields['puit'].widget.attrs['class'] = "form-check-input"
        self.fields['goute_a_goute'].widget.attrs['class'] = "form-check-input"
        self.fields['local_technique'].widget.attrs['class'] = "form-check-input"

        self.fields['genre_marocain'].widget.attrs['class'] = "form-check-input"
        self.fields['genre_contemporain'].widget.attrs['class'] = "form-check-input"
        self.fields['genre_moderne'].widget.attrs['class'] = "form-check-input"
        self.fields['genre_traditionnel'].widget.attrs['class'] = "form-check-input"

        self.fields['chauffeau_electrique'].widget.attrs['class'] = "form-check-input"
        self.fields['chauffeau_gaz'].widget.attrs['class'] = "form-check-input"
        self.fields['climatisation_centrale'].widget.attrs['class'] = "form-check-input"
        self.fields['climatisation_revirsible'].widget.attrs['class'] = "form-check-input"
        self.fields['climatisation_mural'].widget.attrs['class'] = "form-check-input"
        self.fields['parking_collectif'].widget.attrs['class'] = "form-check-input"
        self.fields['parking_prive'].widget.attrs['class'] = "form-check-input"
        self.fields['exclusive'].widget.attrs['class'] = "form-check-input"
        self.fields['occuped'].widget.attrs['class'] = "form-check-input"
        self.fields['libre'].widget.attrs['class'] = "form-check-input"


        self.fields['global_bedrooms'].widget.attrs['type'] = "text"
        self.fields['suite_number'].widget.attrs['type'] = "text"
        self.fields['master_number'].widget.attrs['type'] = "text"
        self.fields['superficie_habitable'].widget.attrs['type'] = "text"
        self.fields['superficie_terrain'].widget.attrs['type'] = "text"
        self.fields['superficie_construite'].widget.attrs['type'] = "text"
        self.fields['superficie_sol'].widget.attrs['type'] = "text"
        self.fields['superficie_terrasse'].widget.attrs['type'] = "text"
        self.fields['superficie_jardin'].widget.attrs['type'] = "text"
        self.fields['superficie_coure'].widget.attrs['type'] = "text"
        self.fields['nbre_salon_marocain'].widget.attrs['type'] = "text"
        self.fields['nbre_salon_european'].widget.attrs['type'] = "text"
        self.fields['nbre_salon_cheminie'].widget.attrs['type'] = "text"
        self.fields['nbre_salon_sejour'].widget.attrs['type'] = "text"
        self.fields['nbre_cuisine_independante'].widget.attrs['type'] = "text"
        self.fields['nbre_cuisine_kitchinette'].widget.attrs['type'] = "text"
        self.fields['nbre_cuisine_americaine'].widget.attrs['type'] = "text"
        self.fields['bathrooms_italienne'].widget.attrs['type'] = "text"
        self.fields['bathrooms_baignoire'].widget.attrs['type'] = "text"
        self.fields['bathrooms_sde'].widget.attrs['type'] = "text"
        self.fields['bathrooms_hammam_beldi'].widget.attrs['type'] = "text"
        self.fields['nbre_terrasse'].widget.attrs['type'] = "text"
        self.fields['nbre_coure'].widget.attrs['type'] = "text"
        self.fields['nbre_balcon'].widget.attrs['type'] = "text"
        self.fields['nbre_c_anglaise'].widget.attrs['type'] = "text"
        self.fields['nbre_terrasse_toit'].widget.attrs['type'] = "text"
        self.fields['nbre_buanderie'].widget.attrs['type'] = "text"
        self.fields['price'].widget.attrs['type'] = "text"
        
        
        
        

        
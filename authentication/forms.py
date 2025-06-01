from django import forms
from django.forms import ModelForm
from .models import Profile, Team
from .utils import validateEmail
from django.contrib.auth.models import User, Group
from django.contrib import  auth


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(
        label="Nouveau mot de passe (laisser vide si inchangé)",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        
        super(UserProfileForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('instance', None)
        
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password and password.strip() != "":
            user.set_password(password)
        else:
            # recharge l'instance originale pour garder l'ancien mot de passe
            if self.instance.pk:
                old_user = User.objects.get(pk=self.instance.pk)
                user.password = old_user.password

        if commit:
            user.save()

        return user



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'profile_type']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.all()
        self.fields['avatar'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
        self.fields['team'].widget.attrs['class'] = "form-select me-4"


from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        required=False  # facultatif si modification
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'groups']
    
    def __init__(self, *args, **kwargs):
        
        super(CustomUserForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('instance', None)
       
        
        #self.fields['avatar'].initial = profile.avatar
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password'].required = True
        
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        if commit:
            user.save()
            self.save_m2m()  # pour les groupes

        return user


class MyProfileForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'password',)
    def __init__(self, *args, **kwargs):
        
        super(MyProfileForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('instance', None)
       
        
        #self.fields['avatar'].initial = profile.avatar
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        
        
        self.fields['password'].required = True
        self.fields['confirm_password'].required = True
        
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    def clean(self):
        cleaned_data = super(MyProfileForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Les mots de passe ne sont pas identiques")



class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'password', 'is_active')
            
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('instance', None)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['is_active'].required = False
        if user:
            self.fields['password'].required = False
            self.fields['confirm_password'].required = False
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['is_active'].widget.attrs['class'] ='form-check-input'
        
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        if self.instance:
            exist = User.objects.filter(email=email).exclude(pk=self.instance.pk).exists()
        else:            
            exist = User.objects.filter(email=email).exists()
        
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Les mots de passe ne sont pas identiques")
            
        if exist:
            self.add_error("email", "Adresse E-mail déjà utilisée")
            
            
       
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(widget=forms.CheckboxInput)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['remember_me'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['remember_me'].widget.attrs['class'] = 'form-check-input'
    def clean(self, *args, **kwargs):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        email = email.lower()
        if not validateEmail(email):
            self.add_error("email", "Adresse E-mail non valide")
        if email and password:
            user = auth.authenticate(username=email, password=password)
            if user:
                if not user.is_active:  
                    self.add_error("email", "Ce compte est désactivé")
            else:
                self.add_error("email", "E-mail ou Mot de Passe Incorrectes")
                
        else:
            self.add_error("email", "Veuillez fournir votre E-mail et Mot de Passe")



class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('team_title',)
    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
           
            visible.field.widget.attrs['class'] = 'mb-2 form-control-sm form-control'
            
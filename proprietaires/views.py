from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from .models import Proprietaire
from .forms import ProprietaireForm
from proprietes.models import Propriete

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list(request):
    list_proprieataires = Proprietaire.objects.all()
    context = {
        'list_proprieataires':list_proprieataires
    }
    return render(request, 'proprietaire/list.html', context=context)


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list_proprietes(request, pk):
   
    proprietaire = get_object_or_404(Proprietaire, pk=pk)

    if proprietaire:
      list_proprietes = Propriete.objects.filter(proprietaire=proprietaire)
      context = {
        'list_proprietes':list_proprietes
      }
      return render(request, 'proprietaire/list-proprietes.html', context=context)

    else :
       return redirect('list-proprietaires')
    
@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def proprietaire_edit (request, pk=None):
  if request.POST:
    
    if not pk:
        proprietaire_form = ProprietaireForm(request.POST)
        
        if proprietaire_form.is_valid():
          proprietaire_form.save()
        else:
          context = {
            'proprietaire_form':proprietaire_form,
          }
          return render(request, 'proprietaire/edit.html', context)
    else:
        proprietaire = Proprietaire.objects.get(pk=pk)
        proprietaire_form = ProprietaireForm(request.POST, instance=proprietaire)
        if proprietaire_form.is_valid():
          proprietaire_form.save()
          

        else:
          proprietaire_form = ProprietaireForm(request.POST)
         
          context = {
            'proprietaire_form':proprietaire_form,
            'pk':pk,
          }
          return render(request, 'proprietaire/edit.html', context)
         
                                      
          
    return redirect('list-proprietaires')
  else:   

    if pk:
      proprietaire = get_object_or_404(Proprietaire, pk=pk)
      proprietaire_form = ProprietaireForm(instance=proprietaire)
      context = {
        'proprietaire_form':proprietaire_form 
      }
    else:
      proprietaire_form = ProprietaireForm

      context = {
        'proprietaire_form':proprietaire_form,

      }
  return render(request, 'proprietaire/edit.html', context)
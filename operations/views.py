from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from .models import Operation
from .forms import OperationForm

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list(request):
    list_operations = Operation.objects.all()
    context = {
        'list_operations':list_operations
    }
    return render(request, 'operation/list.html', context=context)


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def operation_edit (request, pk=None):
  if request.POST:
    
    operation_form = OperationForm(request.POST)
    if operation_form.is_valid():
      if not pk:
        type_operation = operation_form.cleaned_data['type_operation']
        date_operation = operation_form.cleaned_data['date_operation']
        propriete = operation_form.cleaned_data['propriete']
        client = operation_form.cleaned_data['client']
        prix_operation = operation_form.cleaned_data['prix_operation']
        duree_operation = operation_form.cleaned_data['duree_operation']
        monant_commission = operation_form.cleaned_data['monant_commission']
        numero_contrat = operation_form.cleaned_data['numero_contrat']
        

        operation = Operation.objects.create(type_operation=type_operation, 
                                      date_operation=date_operation, 
                                      propriete=propriete, 
                                      client=client,
                                      prix_operation=prix_operation,
                                      duree_operation=duree_operation,
                                      monant_commission=monant_commission,
                                      numero_contrat=numero_contrat)
      else:
         operation = Operation.objects.get(pk=pk)
         operation.type_operation = operation_form.cleaned_data['type_operation']
         operation.date_operation = operation_form.cleaned_data['date_operation']
         operation.propriete = operation_form.cleaned_data['propriete']
         operation.client = operation_form.cleaned_data['client']
         operation.prix_operation = operation_form.cleaned_data['prix_operation']
         operation.duree_operation = operation_form.cleaned_data['duree_operation']
         operation.monant_commission = operation_form.cleaned_data['monant_commission']
         operation.numero_contrat = operation_form.cleaned_data['numero_contrat']

         operation.save()
                                      
          
      return redirect('list-operations')

    else:
      operation_form = OperationForm(request.POST)
      context = {
        'operation_form':operation_form,
        'pk':pk,
      }
    
      return render(request, 'operation/edit.html', context)

  if pk:
    operation_form = OperationForm(instance=get_object_or_404(Operation, pk=pk))
    context = {
      'operation_form':operation_form
    }
  else:
      operation_form = OperationForm
      context = {
        'operation_form':operation_form
      }
  return render(request, 'operation/edit.html', context)
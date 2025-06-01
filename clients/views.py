from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from .models import Client
from .forms import ClientForm

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list(request):
    list_clients = Client.objects.all()
    context = {
        'list_clients':list_clients
    }
    return render(request, 'client/list.html', context=context)


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def client_edit (request, pk=None):
  if request.POST:
    
    if not pk:
        client_form = ClientForm(request.POST)
        
        if client_form.is_valid():
          client_form.save()
        else:
          context = {
            'client_form':client_form,
          }
          return render(request, 'client/edit.html', context)
    else:
        client = Client.objects.get(pk=pk)
        client_form = ClientForm(request.POST, instance=client)
        if client_form.is_valid():
          client_form.save()
          

        else:
          client_form = ClientForm(request.POST)
         
          context = {
            'client_form':client_form,
            'pk':pk,
          }
          return render(request, 'client/edit.html', context)
         
                                      
          
    return redirect('list-clients')
  else:   

    if pk:
      client = get_object_or_404(Client, pk=pk)
      client_form = ClientForm(instance=client)
      context = {
        'client_form':client_form 
      }
    else:
      client_form = ClientForm

      context = {
        'client_form':client_form,

      }
  return render(request, 'client/edit.html', context)
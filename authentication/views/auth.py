from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views.generic import View
from ..utils import url_has_allowed_host_and_scheme, account_activation_token, EmailThread, validateEmail
from ..forms import LoginForm
from ..models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.conf import settings

class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}


  
class LoginView(SuccessURLAllowedHostsMixin, View):
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_authenticated_user = True

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            remember_me = login_form.cleaned_data['remember_me']
            email = email.lower()
            print('email', email)
            user = auth.authenticate(username=email, password=password)
         
            auth.login(request, user)
            if remember_me is True:
                request.session.set_expiry(30 * 24 * 60 * 60)
            else:
                request.session.set_expiry(60 * 60 * 2)
                
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {
            'login_form':login_form
                }
            return render(request, 'auth/login.html', context)
    def get(self, request):
        if self.redirect_authenticated_user and self.request.user.is_authenticated and not self.request.user.is_superuser:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        login_form = LoginForm()
        context = {
            'next': self.get_redirect_url(),
            'login_form':login_form
        }
        return render(request, 'auth/login.html', context)

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('login')



class PasswordResetView(View):
    def get(self, request):
        return render(request, 'auth/forgot-password.html')

    @method_decorator(csrf_protect)
    def post(self, request):
        email = request.POST['email']
        email = email.lower()
        if not validateEmail(email):
            messages.error(
                request, 'Veuillez fournir un email valide')
            return redirect('reset-password')

        if not User.objects.filter(email=email).exists():
            messages.error(
                request, "Aucun compte n'est associé à cet email")
            return redirect('reset-password')

        user = User.objects.get(email=email)

        if not Profile.objects.filter(user=user).exists():
            messages.error(
                request, "Aucun compte n'est associé à cet email")
            return redirect('reset-password')

        if user.is_active == False:
            messages.error(
                request, "Le compte lié à cet email est désactivé")
            return redirect('reset-password')

        current_site = get_current_site(request)
        html_content = render_to_string('emails/password-reset-email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        text_content = render_to_string('emails/password-reset-email.txt', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email_subject = "Réinitialisation du Mot de Passe"
        EmailThread(subject=email_subject,
                    text_content=text_content,
                    html_content=html_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=user.email).start()
        messages.add_message(
            request, messages.INFO, 'Nous vous avons envoyé un e-mail avec un lien pour réinitialiser votre mot de passe')
        return redirect('reset-password')


INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class CompletePasswordChangeView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is None or not account_activation_token.check_token(user, token):
            messages.add_message(
                request, messages.WARNING, "Le lien n'est plus valide, veuillez en demander un nouveau")
            return render(request, 'auth/reset-password.html', status=401)
        return render(request, 'auth/change-password.html', context={'uidb64': uidb64, 'token': token})

    def post(self, request, uidb64, token):
        context = {'uidb64': uidb64, 'token': token}
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            password = request.POST.get('password')
            password2 = request.POST.get('confirm_password')
            if len(password) < 6:
                messages.add_message(
                    request, messages.ERROR, 'Le mot de passe doit comporter au moins 6 caractères')
                return render(request, 'auth/change-password.html', context, status=400)
            if password != password2:
                messages.add_message(
                    request, messages.ERROR, 'Les mots de passe doivent être identiques')
                return render(request, 'auth/change-password.html', context, status=400)
            user.set_password(password)
            user.save()
            messages.add_message(
                request, messages.INFO, 'Mot de passe changé avec succès, connectez-vous avec votre nouveau mot de passe')
            return redirect('login')
        except DjangoUnicodeDecodeError:
            messages.add_message(
                request, messages.ERROR, "Une erreur s'est produite, vous n'avez pas pu mettre à jour votre mot de passe")
            return render(request, 'auth/change-password.html', context, status=401)
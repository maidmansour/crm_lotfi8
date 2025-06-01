from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True

    
class Team(models.Model):
   
    team_title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Equipes"
        
    def __str__(self):
        return self.team_title
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=10, default='USER')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_profile")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Utilisateurs"
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

from django.db import models
from authentication.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # Define model fields.
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    social_security_number = models.CharField(max_length=12)

    # Used internally to display the string representation of the object.
    def __str__(self):
        return self.user.email

    # Listens for user activity.
    @receiver(post_save, sender=User)
    # When a user is created, this will attach a profile to the user.
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    # When user is saved, this will save the profile as well.
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

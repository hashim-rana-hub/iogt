from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    first_name = models.CharField('first name', max_length=150, null=True, blank=True)
    last_name = models.CharField('last name', max_length=150, null=True, blank=True)
    email = models.EmailField('email address', null=True, blank=True)
    terms_accepted = models.BooleanField(default=False)

    has_filled_registration_survey = models.BooleanField(default=False)

    @property
    def is_rapidpro_bot_user(self):
        return self.pk == settings.RAPIDPRO_BOT_USER_ID

    @classmethod
    def get_rapidpro_bot_user(cls):
        return cls.objects.get(pk=settings.RAPIDPRO_BOT_USER_ID)

    class Meta:
        ordering = ('id',)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}\'s profile'


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

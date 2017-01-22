from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class BaiheUserManager(UserManager):

    def create_user(self, username, nickname, password):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
        user = self.create_user(
            username,
            password=password,
            nickname=nickname,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class BaiheUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20, unique=True)

    objects = BaiheUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_superuser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

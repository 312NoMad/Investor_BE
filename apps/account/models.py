import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from utils.models import AbstractModel


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('ID'))
    email = models.EmailField(unique=True, verbose_name=_('email'))

    first_name = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("first name"))
    last_name = models.CharField(max_length=150, blank=True, null=True, verbose_name=_('last name'))

    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    date_joined = models.DateTimeField(default=timezone.now, verbose_name=_('joined date'))

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email


class UserProfile(AbstractModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name=_('Profile User'),
                                related_name='profile')


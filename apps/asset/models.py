from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel

User = get_user_model()


class Portfolio(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio', verbose_name='owner')


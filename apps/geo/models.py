from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel


class Country(AbstractModel):
    name = models.CharField(_('Country'), max_length=255)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class City(AbstractModel):
    name = models.CharField(_('City'), max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name=_('Country'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

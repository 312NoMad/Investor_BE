from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel

User = get_user_model()


class Portfolio(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio', verbose_name='owner')

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')


class PropertyType(AbstractModel):
    name = models.CharField(_('type name'), max_length=255)
    description = models.TextField(_('desction'), blank=True, null=True)

    class Meta:
        verbose_name = _("Property type")
        verbose_name_plural = _("Property types")


class Property(AbstractModel):
    name = models.CharField(_('Name'), max_length=255, blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='properties',
                                      verbose_name=_('property type'))

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")


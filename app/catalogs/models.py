from django.utils.translation import gettext_lazy as _
from django.db import models


class Currency(models.Model):

    charcode = models.CharField(max_length=3, unique=True, verbose_name=_('Код валюты'))
    date = models.DateField(verbose_name=_('Дата'))
    rate = models.DecimalField(max_digits=7, decimal_places=4, verbose_name=_('Курс'))

    class Meta:
        verbose_name = _('Валюта')
        verbose_name_plural = _('Валюты')

    def __str__(self):
        return self.charcode

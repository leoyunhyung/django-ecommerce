# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model


class CategoryGroup(Model):
    name = models.CharField(_('이름'), max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('카테고리 그룹')


class Category(Model):
    category_group = models.ForeignKey('CategoryGroup', verbose_name=_('카테고리 그룹'), on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(_('이름'), max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('카테고리')

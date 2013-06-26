from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from .settings import COLUMN_CHOICES


class Grid(CMSPlugin):
    inner = models.BooleanField(_('inner'), default=True, help_text=_(
        'Defines whether the plugin is already inside a grid container or '
        'another Multi-column plugin.'))
    custom_classes = models.CharField(_('custom classes'), max_length=200,
                                      blank=True)

    def __unicode__(self):
        return _(u"%s columns") % self.cmsplugin_set.all().count()


class GridColumn(CMSPlugin):
    size = models.CharField(_('size'), choices=COLUMN_CHOICES,
                            default='1', max_length=50)
    custom_classes = models.CharField(_('custom classes'), max_length=200,
                                      blank=True)

    def __unicode__(self):
        return u"%s" % self.get_size_display()


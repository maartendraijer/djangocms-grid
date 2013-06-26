from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Grid
from .settings import COLUMN_CHOICES, TOTAL_COLUMNS_CHOICES


class GridPluginForm(forms.ModelForm):
    create = forms.ChoiceField(label=_('Create Columns'),
                               choices=TOTAL_COLUMNS_CHOICES,
                               help_text=_('Create this number of columns '
                                           'inside'))
    create_size = forms.ChoiceField(label=_('Column size'),
                                    choices=COLUMN_CHOICES,
                                    help_text=('Width of created columns. You '
                                               'can still change the width of '
                                               'the column afterwards.'))

    class Meta:
        model = Grid
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')

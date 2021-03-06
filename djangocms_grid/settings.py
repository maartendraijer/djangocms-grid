from django.conf import settings

TOTAL_COLUMNS = getattr(settings, 'DJANGOCMS_GRID_TOTAL_COLUMNS', 24)
TOTAL_COLUMNS_CHOICES = [
    (i, i) for i in range(0, TOTAL_COLUMNS + 1)
]
COLUMN_CHOICES = [
    (str(i), 'grid-{}'.format(i)) for i in range(1, TOTAL_COLUMNS + 1)
]

GRID_COLUMN_PLUGINS = getattr(settings, 'GRID_COLUMN_PLUGINS', None)
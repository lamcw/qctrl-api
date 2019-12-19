from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Control(models.Model):
    """Quantum control."""

    class ControlChoices(models.TextChoices):
        """Choices for quantum control type."""

        PRIMITIVE = 'PRI', _('Primitive')
        CORPSE = 'COR', _('CORPSE')
        GAUSSIAN = 'GSN', _('Gaussian')
        CINBB = 'CBB', _('CinBB')
        CINSK = 'CSK', _('CinSK')

    name = models.CharField(max_length=50,
                            help_text=_('The name of the control.'))
    type = models.CharField(max_length=3,
                            choices=ControlChoices.choices,
                            help_text=_('Quantum control type.'))
    maximum_rabi_rate = models.DecimalField(
        max_digits=8,
        decimal_places=5,
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)],
        help_text=_('Maximum achievable angular frequency of the Rabi cycle '
                    'for a driven quantum transition. 0 <= rate <= 100, max '
                    'decimal places = 5.'))
    polar_angle = models.DecimalField(
        max_digits=6,
        decimal_places=5,
        validators=[MinValueValidator(0),
                    MaxValueValidator(1)],
        help_text=_('An angle measured from the z-axis on the Bloch sphere. '
                    '0 <= polar_angle <= 1, max decimal places = 5.'))

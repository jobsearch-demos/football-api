# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#


""" This module contains the Stadium model. """

from django.db import models
from django.utils.translation import gettext_lazy as _


class Stadium(models.Model):
    """ This model represents a stadium. """

    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
        help_text=_('The name of the stadium.'),
    )

    location = models.CharField(
        max_length=255,
        verbose_name=_('Location'),
        help_text=_('The location of the stadium.'),
    )

    capacity = models.IntegerField(
        verbose_name=_('Capacity'),
        help_text=_('The capacity of the stadium.'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')

# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

""" This module contains the Player model. """

from django.db import models
from django.utils.translation import gettext_lazy as _


class Player(models.Model):
    """ This model contains the information about the player. """

    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=50,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=50,
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        null=True,
        blank=True,
    )
    player_number = models.IntegerField(
        verbose_name=_("Player number"),
        null=False,
        blank=False,
    )
    position = models.CharField(
        verbose_name=_("Position"),
        max_length=50,
        null=True,
        blank=True,
    )
    height = models.FloatField(
        verbose_name=_("Height"),
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        verbose_name=_("Weight"),
        null=True,
        blank=True,
    )
    nationality = models.CharField(
        verbose_name=_("Nationality"),
        max_length=50,
        null=True,
        blank=True,
    )
    contract_until = models.DateField(
        verbose_name=_("Contract until"),
        null=True,
        blank=True,
    )
    market_value = models.FloatField(
        verbose_name=_("Market value"),
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="player/images",
        null=True,
        blank=True,
    )

    def __str__(self):
        """String representation of Player model"""
        return f"{self.first_name} {self.last_name}"

    # pylint: disable=too-few-public-methods
    class Meta:
        """Meta class for Player model"""
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

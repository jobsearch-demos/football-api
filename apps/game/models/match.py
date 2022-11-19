# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

"""This module contains the Match model."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Match(models.Model):
    """Match model."""

    home_team = models.ForeignKey(
        "club.Club",
        on_delete=models.CASCADE,
        related_name="home_team",
        verbose_name=_("Home Team"),
    )
    away_team = models.ForeignKey(
        "club.Club",
        on_delete=models.CASCADE,
        related_name="away_team",
        verbose_name=_("Away Team"),
    )
    match_date = models.DateTimeField(
        verbose_name=_("Match Date"),
    )
    stadium = models.ForeignKey(
        "Stadium",
        on_delete=models.CASCADE,
        verbose_name=_("Stadium"),
    )

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.home_team} vs {self.away_team}"

    # pylint: disable=too-few-public-methods
    class Meta:
        """Meta options."""

        verbose_name = _("Match")
        verbose_name_plural = _("Matches")
        ordering = ["-match_date"]

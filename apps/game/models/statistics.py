# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

"""This module contains the models for the statistics app."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Statistics(models.Model):
    """This class represents the statistics model."""

    game = models.ForeignKey(
        'game.Match',
        on_delete=models.CASCADE,
        related_name='statistics',
        verbose_name=_('Game'),
    )
    club = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='statistics',
        verbose_name=_('Club'),
    )
    goals = models.IntegerField(
        verbose_name=_('Goals'),
        help_text=_('The number of goals scored by the club.'),
    )
    assists = models.IntegerField(
        verbose_name=_('Assists'),
        help_text=_('The number of assists made by the club.'),
    )
    yellow_cards = models.IntegerField(
        verbose_name=_('Yellow Cards'),
        help_text=_('The number of yellow cards received by the club.'),
    )
    red_cards = models.IntegerField(
        verbose_name=_('Red Cards'),
        help_text=_('The number of red cards received by the club.'),
    )
    off_side = models.IntegerField(
        verbose_name=_('Off Side'),
        help_text=_('The number of off sides made by the club.'),
    )
    shots_on_target = models.IntegerField(
        verbose_name=_('Shots On Target'),
        help_text=_('The number of shots on target made by the club.'),
    )
    shots_off_target = models.IntegerField(
        verbose_name=_('Shots Off Target'),
        help_text=_('The number of shots off target made by the club.'),
    )
    ball_possession = models.FloatField(
        verbose_name=_('Ball Possession'),
        help_text=_('The number of ball possession made by the club.'),
    )
    shots_blocked = models.IntegerField(
        verbose_name=_('Shots Blocked'),
        help_text=_('The number of shots blocked by the club.'),
    )
    corner_kicks = models.IntegerField(
        verbose_name=_('Corner Kicks'),
        help_text=_('The number of corner kicks made by the club.'),
    )

    def __str__(self):
        return f'{self.club} - {self.game}'

    class Meta:
        verbose_name = _('Statistics')
        verbose_name_plural = _('Statistics')
        unique_together = ('game', 'club')

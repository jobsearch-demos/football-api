# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#


""" This module contains the Club Statistics model. """

from django.db import models
from django.utils.translation import gettext_lazy as _


class ClubStatistics(models.Model):
    """ This model represents a club statistics. """

    club = models.OneToOneField(
        to='club.Club',
        on_delete=models.CASCADE,
        verbose_name=_('Club'),
        help_text=_('The club.'),
    )
    games = models.ManyToManyField(
        to='game.Match',
        verbose_name=_('Games'),
        help_text=_('The games played by the club.'),
    )
    games_played = models.IntegerField(
        verbose_name=_('Games Played'),
        help_text=_('The number of games played by the club.'),
    )
    games_won = models.IntegerField(
        verbose_name=_('Games Won'),
        help_text=_('The number of games won by the club.'),
    )
    games_drawn = models.IntegerField(
        verbose_name=_('Games Drawn'),
        help_text=_('The number of games drawn by the club.'),
    )
    games_lost = models.IntegerField(
        verbose_name=_('Games Lost'),
        help_text=_('The number of games lost by the club.'),
    )
    goals_scored = models.IntegerField(
        verbose_name=_('Goals Scored'),
        help_text=_('The number of goals scored by the club.'),
    )
    goals_conceded = models.IntegerField(
        verbose_name=_('Goals Conceded'),
        help_text=_('The number of goals conceded by the club.'),
    )
    goal_difference = models.IntegerField(
        verbose_name=_('Goal Difference'),
        help_text=_('The goal difference of the club.'),
    )
    points = models.IntegerField(
        verbose_name=_('Points'),
        help_text=_('The number of points of the club.'),
    )

    def __str__(self):
        return self.club.name

    class Meta:
        verbose_name = _('Club Statistics')
        verbose_name_plural = _('Clubs Statistics')

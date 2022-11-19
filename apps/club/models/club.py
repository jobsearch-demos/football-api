# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

"""Models for club app"""
from django.db import models


# Club model represents a football club
class Club(models.Model):
    """Club model"""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    emblem = models.ImageField(upload_to='club/emblems', blank=True, null=True)
    players = models.ManyToManyField('member.Player', related_name='clubs')
    staff = models.ManyToManyField('member.Staff', related_name='clubs')
    stadium = models.OneToOneField(
        'stadium.Stadium',
        on_delete=models.SET_NULL,
        related_name='club',
        blank=True,
        null=True,
    )

    def __str__(self):
        """String representation of Club model"""
        return self.name

    class Meta:
        """Meta class for Club model"""
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

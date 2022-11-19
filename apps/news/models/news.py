# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

""" This module contains the News model. """

from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """ This model represents a news. """

    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
        help_text=_('The title of the news.'),
    )
    content = models.TextField(
        verbose_name=_('Content'),
        help_text=_('The content of the news.'),
    )
    category = models.CharField(
        max_length=255,
        verbose_name=_('Category'),
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        help_text=_('The image of the news.'),
    )
    created_at = models.DateTimeField(
        verbose_name=_('Published at'),
        help_text=_('The published at of the news.'),
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Edited at'),
        help_text=_('The edited at of the news.'),
    )

    def __str__(self):
        """ This method returns the title of the news. """
        return f'{self.title}'

    # pylint: disable=too-few-public-methods
    class Meta:
        """ This class contains the meta information of the News model. """
        verbose_name = _('News')
        verbose_name_plural = _('News')

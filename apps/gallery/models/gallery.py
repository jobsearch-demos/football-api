# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#


""" This module contains the Gallery model. """

from django.db import models
from django.utils.translation import gettext_lazy as _


class Gallery(models.Model):
    """ This model represents a gallery. """

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("The title of the gallery."),
    )

    def __str__(self):
        """ Return the title of the gallery. """
        return f'{self.title}'

    # pylint: disable=too-few-public-methods
    class Meta:
        """ Meta class. """
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')


class GalleryImage(models.Model):
    """ This model represents a gallery image. """

    gallery = models.ForeignKey(
        "gallery.Gallery",
        on_delete=models.CASCADE,
        verbose_name=_("Gallery"),
    )
    image = models.ImageField(
        upload_to="gallery",
        verbose_name=_("Image"),
        help_text=_("The image of the gallery."),
    )

    def __str__(self):
        """ Return the title of the gallery. """
        return f'{self.image.name}'

    # pylint: disable=too-few-public-methods
    class Meta:
        """ Meta class. """
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')

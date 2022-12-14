# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

""" This module contains the CMSHome model. """

from django.db import models
from django.utils.translation import gettext_lazy as _


class CMSHome(models.Model):
    """ This model represents the home page. """

    gallery = models.ForeignKey(
        "gallery.Gallery",
        on_delete=models.CASCADE,
        verbose_name=_("Gallery"),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("The title of the home page."),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('CMS Home')
        verbose_name_plural = _('CMS Homes')

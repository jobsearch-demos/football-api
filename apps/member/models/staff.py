# @copyright Copyright (c) 2022 Kamran Valijonov.
# All rights reserved.
# Kamran Valijonov is a software engineer and a computer scientist.
# He is the author of the current software.
# This software is a confidential trade secret of Kamran Valijonov.
# Use, examination, reproduction, copying, transfer and/or disclosure
# to others of all or any part of this software are prohibited except
# with the express written consent of Kamran Valijonov.
#

"""This module contains the Staff model."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class StaffCategoryOptions(models.TextChoices):
    """This class contains the StaffCategoryOptions."""

    COACH = "COACH", _("Coach")
    OWNER = "OWNER", _("Owner")


class Staff(models.Model):
    """This class represents the Staff model."""
    first_name = models.CharField(
        max_length=255,
        verbose_name=_('First name'),
        help_text=_('The first name of the staff.'),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_('Last name'),
        help_text=_('The last name of the staff.'),
    )
    date_of_birth = models.DateField(
        verbose_name=_('Date of birth'),
        help_text=_('The date of birth of the staff.'),
    )
    nationality = models.CharField(
        max_length=255,
        verbose_name=_('Nationality'),
        help_text=_("The nationality of the staff."),
    )
    category = models.CharField(
        max_length=255,
        verbose_name=_('Category'),
        help_text=_('The category of the staff.'),
        choices=StaffCategoryOptions.choices,
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        help_text=_('The email of the staff.'),
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name=_('Phone number'),
        help_text=_('The phone number of the staff.'),
    )

    def __str__(self):
        """This method returns the string representation of the Staff model."""
        return f"{self.first_name} {self.last_name}"

    # pylint: disable=too-few-public-methods
    class Meta:
        """This class contains the meta information of the Staff model."""
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')

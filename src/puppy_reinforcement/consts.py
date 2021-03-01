# -*- coding: utf-8 -*-

# Puppy Reinforcement Add-on for Anki
#
# Copyright (C) 2016-2020  Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.
"""
Addon-wide constants
"""

from ._version import __version__
from .libaddon.platform import checkAnkiVersion

__all__ = ["ADDON"]

USES_LEGACY_HOOKS = not checkAnkiVersion("2.1.20")

# PROPERTIES DESCRIBING ADDON


class ADDON(object):
    """Class storing general add-on properties
    Property names need to be all-uppercase with no leading underscores
    """

    NAME = "Puppy Reinforcement for Sanika"
    MODULE = "puppy_reinforcement_for_sanika"
    VERSION = __version__
    LICENSE = "GNU AGPLv3"
    AUTHORS = ({
        "name": "Sanika Rane & Thomas Herring",
        "years": "2021",
        "contact": "https://github.com/th3rring",
    }, )
    AUTHOR_MAIL = "teh6@rice.edu"
    LIBRARIES = ()
    CONTRIBUTORS = ("zjosua", "glutanimate")
    SPONSORS = ()
    LINKS = {}

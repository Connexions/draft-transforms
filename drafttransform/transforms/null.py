# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""Do nothing"""

__all__ = ('cli_loader',)


def cli_command(cnxml,**kwargs):
    """The command used by the CLI to invoke the transform logic."""
    return 


def cli_loader(parser):
    """Used to load the CLI toggles and switches, returns command"""
    return cli_command

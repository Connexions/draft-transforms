# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""Download document"""

__all__ = ('cli_loader',)


def cli_command(cnxml,**kwargs):
    """The command used by the CLI to invoke the transform logic."""
    return cnxml


def cli_loader(parser):
    """Used to load the CLI toggles and switches, returns command"""
    parser.add_argument('save_dir_d', metavar="save_dir", nargs="?",
                        help="directory to save documents to")
    return cli_command

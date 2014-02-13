# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""apply an xslt transform to each document"""

from lxml import etree

__all__ = ('cli_loader',)


def cli_command(cnxml,**kwargs):
    """The command used by the CLI to invoke the transform logic."""
    with open(kwargs['xslt']) as xf:
        xsl=etree.parse(xf).getroot()
        transform=etree.XSLT(xsl)
        xml=etree.XML(cnxml)
    return unicode(transform(xml)).encode('utf-8')


def cli_loader(parser):
    """Used to load the CLI toggles and switches."""
    parser.add_argument('xslt', 
                        help="be converted")
    parser.add_argument('save_dir_d', metavar="save_dir", nargs="?",
                        help="directory to save transformed documents to")
    return cli_command

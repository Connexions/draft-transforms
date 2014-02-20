# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""\
Package that houses the individual transform steps as modules.

The utilities found in the root of this package provide magical
functionality for transform CLI loading, default transform discover,
and transform registration.

Transforms in this package are required to have a ``cli_loader``
function that is given a subparser to add additional parsing options,
if necessary, and must return a filter function. This function will be
called with the parsed arguments as keyword paramaters, as well as the
file to transform as the first positional parameter, and are expected
to return the transformed data, or None, to indicate skipping that
transform.  (conventionally named, ``xform_command``). 

"""
import sys
import os


__all__ = ('load_cli', 'get_default',)


# Transform discovery is magical. Anything that ends in .py and doesn't start
# with __ will be expected to be a transformation, taking a cnxml document as
# its first param, and returning a transformed doc

here=os.path.dirname(__file__)
TRANSFORMS = [f[:-3] for f in os.listdir(here) if f.endswith('.py') and not f.startswith('__')]

# TODO Look this up via setuptools entry-point so that it only needs to be
#      changed at the distribution level on say release or tag.
DEFAULT_TRANSFORM = 'null'


def _import_attr_n_module(module_name, attr):
    """From the given ``module_name`` import
    the value for ``attr`` (attribute).
    """
    __import__(module_name)
    module = sys.modules[module_name]
    attr = getattr(module, attr)
    return attr, module

def _import_loader(module_name):
    """Given a ``module`` name import the cli loader."""
    loader, module = _import_attr_n_module(module_name, 'cli_loader')
    return loader, module.__doc__


def load_cli(subparsers):
    """Given a parser, load the transforms as CLI subcommands"""
    for transform_name in TRANSFORMS:
        module = 'drafttransform.transforms.{}'.format(transform_name)
        loader, description = _import_loader(module)
        parser = subparsers.add_parser(transform_name,
                                       help=description)
        command = loader(parser)
        if command is None:
            raise RuntimeError("Failed to load '{}'.".format(transform_name))
        parser.set_defaults(cmmd=command)


def get_default_cli_command_name():
    """Discover and return the default transform name (same as the
    subcommand name).
    """
    return DEFAULT_TRANSFORM

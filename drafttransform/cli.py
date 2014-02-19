#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2013, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""The command-line interface for transforming cnxml files directly in workspace."""
import os
import sys
import argparse

from . import transforms
from workgroup import Workgroup, listWorkspaces

DESCRIPTION = __doc__
DEFAULT_HOST = "qa.cnx.org"


def main(argv=None):
    """Main functions used to interface directly with the user."""
    parser = argparse.ArgumentParser(description = DESCRIPTION)
    parser.add_argument('-H', '--host',
                        default = DEFAULT_HOST,
                        help = "A legacy connexions authoring site")
    parser.add_argument('-a', '--auth', required = True,
                        help = "authentication info [userid:password]")
    parser.add_argument('-w', '--workgroup',
                        help = "Id of workgroup: defaults to user's private workspace")
    parser.add_argument('-l', '--list',
                        action = "store_true",
                        help = "List all workspaces")
    parser.add_argument('-p', '--publish', metavar = 'message',
                        help = "Publish after transform")
    parser.add_argument('-P', '--publish_only', metavar = 'message',
                        help = "Publish all drafts, no download or transform")
    parser.add_argument('-u', '--upload',
                        action = "store_true",
                        help="Upload transformed doc back to draft")
    parser.add_argument('-s', '--save-dir',
                        help = "Directory to save transformed output to, as <moduleid>.xml")
    subparsers = parser.add_subparsers(help = "transform step")
    transforms.load_cli(subparsers)

    if len(sys.argv) < 5 or sys.argv[0].startswith('-'):
        sys.argv.append(transforms.get_default_cli_command_name())
        print sys.argv
    args = parser.parse_args(argv)
    
    if hasattr(args,'save_dir') and args.save_dir or hasattr(args,'save_dir_d') and args.save_dir_d:
        save_dir = args.save_dir or args.save_dir_d 
    else:
        save_dir = None

    cmmd = args.cmmd

    if args.list:
        print '\n'.join(listWorkspaces(**vars(args)))
        return
    # walk workgroup, look over and retrieve cnxmls, transform, then save and
    # optionally publish.

    workgroup = Workgroup(**vars(args))
    print workgroup.url
    for mod in workgroup.modules():
        if args.publish_only:
            mod.publish(args.publish_only)
        else:
            cnxml = mod.cnxml()
            new_cnxml = cmmd(cnxml,**vars(args))
            if cnxml and new_cnxml:
                print '%s: %s %s' % (mod.moduleid,len(cnxml),len(new_cnxml))
                if save_dir:
                    if not os.path.exists(save_dir):
                        os.mkdir(save_dir)
                    with open(os.path.join(save_dir,'%s.xml' % (mod.moduleid)), 'w') as m:
                        m.write(new_cnxml)
                if args.upload:
                    mod.save(new_cnxml)
                if args.publish:
                    mod.publish(args.publish)

    
    return # cmmd(**vars(args))


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""Models to wrap the legacy workgroup and provide behaviors"""

from requests_toolbelt import MultipartEncoder
import requests
import re
import textwrap



class Module:
    """Class to provide methods to retrieve and save content from RME"""
    def __init__(self, moduleid, workgroup):
        self.moduleid = moduleid
        self.workgroup = workgroup
        self.url = '/'.join((self.workgroup.url, self.moduleid))
        self.auth = self.workgroup.auth

    def cnxml(self):
        """Fetch the cxnml (checkout if necessary)"""
        r = requests.get('%s/index.cnxml' % self.url, auth=self.auth)
        if not r: # perhaps need to checkout
            r = requests.post('%s/content_checkout' % self.url, auth=self.auth)
            r = requests.get('%s/index.cnxml' % self.url, auth=self.auth)
        if r:
            return r.content
        else:
            return None
            
    def save(self,cnxml):
        """Push new cnxml to RME"""
        data = MultipartEncoder(fields={'importFile':('index.cnxml', cnxml.decode('utf-8')),
            'format':'plain', 'submit':'Import', 'form.submitted':'1',
            'came_from':'module_text'})
        r = requests.post('%s/module_import_form' % self.url, data = data.to_string(), 
            auth = self.auth, headers = {'Content-Type': data.content_type})

    def publish(self, message=None):
        """Publish module"""
        print "publishing %s: %s" % (self.moduleid, message), 
        data = {'message':message,'form.button.publish':'Publish','form.submitted':'1'}
        r = requests.post('%s/module_publish_description' % self.url, data = data, auth = self.auth)
        if not r.history or 'Item%20Published' not in r.history[-1].url:
                print "failed: see %s" % (self.url+'/module_publish')
        else:
                print "success"


class Workgroup:
    """Class that wraps a workgroup to provide access to module editors"""

    def __init__(self, host=None, auth=None, workgroup=None, **kwargs):
        self.host = host
        self.auth = tuple(auth.split(':'))
        self.workgroupid = workgroup
        self.mod_ids = None
        if host.startswith('127.') or host == 'localhost':
            protocol = 'http'
        else:
            protocol = 'https'

        if self.workgroupid:
            self.url = '%s://%s/GroupWorkspaces/%s' % (protocol, host, self.workgroupid)
        else:
            self.url = '%s://%s/Members/%s' % (protocol, host, self.auth[0])
            

    def modules(self, update=False):
        """Walk the workgroup and return wrappers for each Rhaptos Module Editor"""
        if not (self.mod_ids) or update:
            r = requests.get('%s/listFolderContents' % self.url, 
                        params={'spec':'Module Editor'}, auth=self.auth)
            oblist = r.content[1:-1].split(', ')
            self.mod_ids = [m[1:-1].split('/')[-1] for m in oblist]
        for modid in  self.mod_ids:
            yield Module(modid,self)


def listWorkspaces(host=None, auth=None, **kwargs):
    """List all the users Workspaces"""
    if host.startswith('127.') or host == 'localhost':
        protocol = 'http'
    else:
        protocol = 'https'
    
    auth = tuple(auth.split(':'))

    workspaces  = ['%s\tPersonal Workspace (default)' % (auth[0])]

    r = requests.get('%s://%s/getWorkspaces' % (protocol,host), auth=auth )
    if r:
        folder_regex = re.compile("'folder': <[^>]*>,")
        workgroups = eval(folder_regex.sub('',r.content))
        for wg in workgroups:
            prefix='%(id)s\t%(title)s  - ' % wg
            workspaces.append(textwrap.fill(wg['description'], initial_indent=prefix, subsequent_indent=' '*len(prefix)))
    return workspaces
    

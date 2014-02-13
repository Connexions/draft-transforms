#r=requests.get('http://qa.cnx.org/Members/Crouton/listFolderContents', params={'spec':'Module Editor'}, auth=('Crouton','ODeath'))
#clist=r.content[1:-1].split(', ')
#clist[0][1:-1].split('/')[-1]
#r=requests.get('http://qa.cnx.org/Members/Crouton/m13519/index.cnxml', auth=('Crouton','ODeath'))
#r.status_code
#r.ok
#r=requests.post('http://qa.cnx.org/Members/Crouton/m13519/content_checkout', auth=('Crouton','ODeath'))
#r
#data=MultipartEncoder(fields={'importFile':('index.cnxml','some text'),'format':'plain','submit':'Import','form.submitted':'1','came_from':'module_text'})
#r=requests.post('http://qa.cnx.org/Members/Crouton/m13519/module_import_form', data=data, auth=('Crouton','ODeath'))
#data=MultipartEncoder(fields={'importFile':('index.cnxml','some other text'),'format':'plain','submit':'Import','form.submitted':'1','came_from':'module_text'})
#r=requests.post('https://qa.cnx.org/Members/Crouton/m13519/module_import_form', data=data.to_string(), auth=('Crouton','ODeath'), headers={'Content-Type': data.content_type})
#r
#r.history

from requests_toolbelt import MultipartEncoder
import requests

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
        data = MultipartEncoder(fields={'importFile':('index.cnxml', cnxml, 'text/xml'),
            'format':'plain', 'submit':'Import', 'form.submitted':'1',
            'came_from':'module_text'})
        data.to_string()
        r = requests.post('%s/module_import_form' % self.url, data=data, auth=self.auth)

    def publish(self):
        """Publish module"""
        pass

class Workgroup:
    """Class that wraps a workgroup to provide access to module editors"""

    def __init__(self, host=None, auth=None, workgroup=None, **kwargs):
        self.host = host
        self.auth = tuple(auth.split(':'))
        self.workgroupid = workgroup
        self.mod_ids = None

        if self.workgroupid:
            self.url = 'https://%s/GroupWorkspaces/%s' % (host,self.workgroupid)
        else:
            self.url = 'https://%s/Members/%s' % (host,self.auth[0])
            

    def modules(self, update=False):
        """Walk the workgroup and return wrappers for each Rhaptos Module Editor"""
        if not (self.mod_ids) or update:
            r = requests.get('%s/listFolderContents' % self.url, 
                        params={'spec':'Module Editor'}, auth=self.auth)
            oblist = r.content[1:-1].split(', ')
            self.mod_ids = [m[1:-1].split('/')[-1] for m in oblist]
        for modid in  self.mod_ids:
            yield Module(modid,self)



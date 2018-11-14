import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def interface_call(username='', password='', url="https://localhost:9999", path="/", sesh=requests.Session(), conf_file='/root/roxentools_conf.json', ):
    if (username == '' or password == '') and conf_file:
        try:
            with open(conf_file) as filein:
                conf = json.load(filein)
                username = conf['username']
                password = conf['password']
        except IOError:
            print('username or password not provided or could read file %s', conf_file)
            raise

    if username != '' and password != '':
        request_url = url + path

        
        auth = sesh.get(url + "/", auth=(username, password), verify=False)
        wizardid = sesh.cookies['RoxenHttpsWizardId']
        wizard_url = request_url + "&_roxen_wizard_id=" + wizardid
        response = sesh.get(wizard_url, auth=(username, password), verify=False)

        return response

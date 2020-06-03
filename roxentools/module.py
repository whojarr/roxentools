import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def reload(username=None, password=None, host="https://localhost:9999", site="test", module="rxmltags", copy=0):
    """
    tested modules to reload
    rxmltags
    webhaven (inhouse)
    webhaven_pml
    webhaven_rc_handler (inhouse)
     
    """
    usite = quote(site.replace("_", " "))
    url = host + "/rest/configurations/" + usite + "/modules/" + module + "%21" + str(copy) + "/actions/Reload"

    response = requests.put(url, auth=(username, password), verify=False, headers={"X-Roxen-API":"1"})
    if not response.text.strip() == "1":
        return response.json()
    else:
        result = {}
        result['result'] = 'reloaded'
        return result


def add(username=None, password=None, host="https://localhost:9999", site="test", module="rxmltags", copy=0):
    """
    tested modules to add
    
    static_resources
     
    """
    usite = quote(site.replace("_", " "))
    url = host + "/rest/configurations/" + usite + "/modules/" + module + "/"

    response = requests.post(url, auth=(username, password), verify=False, headers={"X-Roxen-API":"1"})
    if not response.text.strip() == "1":
        return json.loads(response.text)
    else:
        return None


def installed(username=None, password=None, host="https://localhost:9999", site="test", module="rxmltags", copy=0):
    """
    tested modules to add
    
    static_resources
     
    """
    usite = quote(site.replace("_", " "))
    url = host + "/rest/configurations/" + usite + "/modules/"

    response = requests.get(url, auth=(username, password), verify=False, headers={"X-Roxen-API":"1", "Content-Type":"application/json"})
    modules = json.loads(response.text)
    if "{}!0".format(module) in modules:
        return True

    return False


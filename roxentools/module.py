import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def reload(username=None, password=None, host="https://localhost:9999", site="test", module="rxmltags", copy=0):
    """
    tested modules to reload
    
    rxmltags
    webhaven (inhouse)
    webhaven_rc_handler (inhouse)
     
    """
    usite = urllib.quote(site.replace("_", " "))
    url = host + "/rest/configurations/" + usite + "/modules/" + module + "%21" + str(copy) + "/actions/Reload"
    response = requests.put(url, auth=(username, password), verify=False, headers={"X-Roxen-API":"1"})
    if not response.text.strip() == "1":
        raise ValueError(response.json()['error'])

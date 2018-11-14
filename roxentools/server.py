from . import interface
import requests
from lxml import html

def server_version():
    return u'Retrun the Roxen Server Version'

def server_restart(url=None, username='', password='', path='', conf_file=None, ):

    sesh = requests.Session()

    response = interface.interface_call(url=url, username=username, password=password, \
                                     path="/actions/?action=restart.pike&class=maintenance", sesh=sesh, conf_file=conf_file, )
    restart_url = None
    anchors = []
    try:
        tree = html.fromstring(response.content)
        anchors = tree.xpath('//a')
    except:
        return "response invalid"
    for anchor in anchors:
        href = anchor.attrib['href']
        if href.startswith('?what=restart&action=restart.pike&class=maintenance&'):
            restart_url = href

    if restart_url:
        restart_response = interface.interface_call(url=url, username=username, password=password, \
                                     path="/actions/" + restart_url, sesh=sesh,  conf_file=conf_file, )
        if restart_response.status_code == 200:
            return "restarted" 
    
    return "Restart Failed"
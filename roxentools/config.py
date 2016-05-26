
import os
import sys
import lxml
from lxml import etree

def domainfromurl(url):
    x = url.replace('https://', '')
    y = x.split('/')
    return y[0]

def nobindfromurl(url):
    x = url.split(';')
    return x[1].replace('nobind=','')

def ipfromurl(url):
    x = url.replace('https://', '')
    return True

def url_split(url):
    result = {"url": "", 'domain': '', "ip": "", "nobind": 0}
    result["url"] = url
    result["domain"] = domainfromurl(url)
    result['nobind'] = nobindfromurl(url)
    return result

def config_files():
    config_folder = '/usr/local/roxen/configurations/'
    result = []
    for item in os.listdir(config_folder):
        if not item.endswith('~') and not item == 'Administration_Interface' and not item == '_roxen_pid' and not item == 'Global_Variables':
            file_path = os.path.join(config_folder, item)
            if os.path.isfile(file_path):
                result.append(item)
    return result

def url_list(sitename):

    urls = []

    filename = '/usr/local/roxen/configurations/' + sitename
    with open(filename, 'r') as f:
        try:
            s = f.read()
            s = "<root>"+s+"</root>"
            parser = etree.XMLParser(ns_clean=True, recover=True)
            tree = etree.fromstring(unicode(s, "utf-8", errors='ignore'), parser)

            for region in tree.iterfind("roxen-config/region"):
                for key,value in region.items():

                    if value.startswith('spider'):
                        for child in region:
                            for key,value in child.items():
                                if value == 'URLs':
                                    for url in child[0]:
                                        url_result = {'url': '','domain': '', 'ip': '', 'nobind': ''}
                                        split_url = url_split(url.text)
                                        url_result['url'] = split_url['url']
                                        url_result['domain'] = split_url['domain']
                                        url_result['ip'] = 0
                                        url_result['nobind'] = split_url['nobind']

                                        if url_result['url'] != '':
                                            urls.append(url_result)
        except Exception, e:
            print "Could not parse:" + filename + ' ' + str(sys.exc_info()[1])

    return urls

def mountpoint_list(sitename):

    mountpoints = []

    filename = '/usr/local/roxen/configurations/' + sitename
    with open(filename, 'r') as f:
        try:
            s = f.read()
            s = "<root>"+s+"</root>"
            parser = etree.XMLParser(ns_clean=True, recover=True)
            tree = etree.fromstring(unicode(s, "utf-8", errors='ignore'), parser)

            for region in tree.iterfind("roxen-config/region"):
                for key,value in region.items():

                    if value.rpartition('#')[0] == 'filesystem':
                        mountpoint_result = {'mountpoint': '', 'searchpath': ''}
                        for child in region:
                            for key,value in child.items():
                                mountpoint=''
                                searchpath=''
                                if value == 'mountpoint':
                                    mountpoint = child[0].text
                                    mountpoint_result['mountpoint'] = mountpoint
                                if value == 'searchpath':
                                    searchpath = child[0].text
                                    mountpoint_result['searchpath'] = searchpath

                        mountpoints.append(mountpoint_result)

        except Exception, e:
            print "Could not parse:" + filename + ' ' + str(sys.exc_info()[1])

    return mountpoints
import os

def site_exists(sitename):
    return os.path.isfile('/usr/local/roxen/configurations/' + sitename)

def site_config_copy(sitename,destination):
    if site_exists(sitename,folder):
        shutil.move('/usr/local/roxen/configurations/' + sitename, destination + '/' + sitename + '_roxen.conf')

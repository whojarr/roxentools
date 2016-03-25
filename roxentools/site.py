import os


def site_exists(sitename):
    return os.path.isfile('/usr/local/roxen/configurations/' + sitename)

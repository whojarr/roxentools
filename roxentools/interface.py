import urllib2
import base64
import json

def interface_call(username='', password='', url="https://localhost:9999", path="/",):

    if username == '' or password == '':
        try:
            with open('/root/roxentools_conf.json') as filein:
                conf = json.load(filein)
                username = conf['username']
                password = conf['password']
        except IOError:
            print('username or password not provided or could read file /root/roxentools_conf.json')
            raise

    if username != '' and password != '':
        request_url = url + path
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        try:
            request = urllib2.Request(request_url)
            request.add_header("Authorization", "Basic %s" % base64string)
            response = urllib2.urlopen(request)
            #print 'response headers: "%s"' % response.info()
        except IOError, e:
            if hasattr(e, 'code'): # HTTPError
                print 'http error code: ', e.code
            elif hasattr(e, 'reason'): # URLError
                print "can't connect, reason: ", e.reason
            else:
                raise
#from urllib import request , parse, error
import urllib
import urllib2
import ssl
import json

def get(url):
    urlDetails = url.split(':')
    sslMode = urlDetails[0] == "https"

    response = ""
    if sslMode:
        cert = ssl.get_server_certificate( ('localhost', 443) )
        open('serv.crt','w').write(cert)


        ctx = ssl.create_default_context()
        ctx.load_verify_locations("serv.crt")
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        try:
            response = urllib.urlopen(url, context=ctx).read().decode("utf8")
        except ssl.SSLError as err:
            print('SSL connection failed: ' + str(err))
        except error.URLError as err:
            print('URL ERROR failed: ' + str(err))
            

    else:
        response = urllib.urlopen(url).read().decode("utf8")

    return response

def post(url, body):
    urlDetails = url.split(':')
    sslMode = urlDetails[0] == "https"

    data = json.dumps(body).encode('utf8')

    response = ""
    if sslMode:
        cert = ssl.get_server_certificate( ('localhost', 443) )
        open('serv.crt','w').write(cert)

        ctx = ssl.create_default_context()
        ctx.load_verify_locations("serv.crt")
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = request.Request(url, data)
        req.add_header('Content-Type', 'application/json')

        try:
            response = request.urlopen(req, context=ctx).read().decode("utf8")
        except ssl.SSLError as err:
            print('SSL connection failed: ' + str(err))
        except error.URLError as err:
            print('URL ERROR failed: ' + str(err))
    else:
        req = urllib2.Request(url, data)
        req.add_header('Content-Type', 'application/json')

        response = urllib.urlopen(req).read().decode("utf8")

    return response
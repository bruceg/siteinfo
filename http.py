from httplib import HTTP

class patterns:
    attempts = []

def identify(host):
    h = HTTP(host)
    h.putrequest('GET', 'http://%s/' % host)
    h.putheader('Accept', '*/*')
    h.endheaders()
    errcode, errmsg, response = h.getreply()
    h.close()
    patterns.attempts = response.headers
    try: str = response['server']
    except: str = None
    return (str, None)


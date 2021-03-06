#!/usr/bin/python
import cgi
import sys
import socket
import time
import os
import string

import http
import nntp
import pop3
import smtp
import imap
import ftp

import websites

mailto_unknown = 'lists-unknown-server@bruce-guenter.dyndns.org'

def log(msg):
    date = time.localtime(time.time())
    try: os.mkdir("log/%04d" % date[0])
    except: pass
    try: os.mkdir("log/%04d/%02d" % date[0:2])
    except: pass
    try:
        out = open("log/%04d/%02d/%02d" % date[0:3], 'a')
        out.write("%02d:%02d:%02d %s\n" % (date[3], date[4], date[5], msg))
        out.close()
    except: pass

services = (
    [ ftp,  "FTP",  "", "" ],
    [ http, "HTTP", "", "" ],
    [ imap, "IMAP", "", "" ],
    [ nntp, "NNTP", "", "" ],
    [ pop3, "POP3", "", "" ],
    [ smtp, "SMTP", "", "" ]
    )

MSG_ERROR = """<html>
<head><title>Error processing your request</title></head>
<body><p>The following error occurred while processing your request:
<pre>%s</pre></p>
</body>
</html>
"""

def error(msg):
    print MSG_ERROR % msg
    sys.exit(0)

HTML_HEAD = """<html>
<head>
<title>Site Software Identification for '%(host)s' (%(ip)s)</title>
</head>
<body>
<p><h1><center>Site Software Identification for '%(host)s' (%(ip)s)</center></h1></p>

<p>Please direct all comments and especially omissions to
<a href=\"mailto:bruce@untroubled.org\">Bruce Guenter</a>.</p>

<p>"""

def main():
    form = cgi.FieldStorage()

    if not form.has_key('host'):
        error("Missing form input 'host'")

    host = form['host'].value
    all = form.has_key('ALL')

    try:
        ip = socket.gethostbyname(host)
    except:
        error("Host not found.")

    print HTML_HEAD % vars()

    for service in services:
        if all or form.has_key(service[1]):
            print "Identifying %s service...<br>" % service[1]
            sys.stdout.flush()
            try:
                response = service[0].identify(ip) or (None, None)
            except:
                response = ('Connection failed', None)
	    service[2] = response[0]
	    service[3] = response[1]

    print "</p>"
    print "<table border=1>"
    print "<tr>"
    print "<th>Service</th>"
    print "<th>Software</th>"
    print "</tr>"

    #logmsg = host
    #for service in services:
    #    if all or form.has_key(service[1]):
    #        logmsg = "%s %s" % (logmsg, service[1])
	#log(logmsg)

    for service in services:
        if all or form.has_key(service[1]):
	    name = service[2] or 'Unknown'
	    version = service[3] or ''
            print "<tr><td align=center>%s</td>" % service[1]
	    link = websites.find(name)
	    if link:
	        print "<td><a href=\"%s\">%s</a> %s</td></tr>" % (
		    link, name, version )
	    else:
	        print "<td>%s %s</td></tr>" % ( name, version )

    print "</table><hr>"

    for service in services:
        if (all or form.has_key(service[1])) and not service[2]:
            pipe = os.popen("/usr/sbin/sendmail -t", "w")
            pipe.write("To: <%s>\n"
                       "Subject: Unknown %s on '%s'\n"
                       "\n"
                       "Response strings were:\n" % (
                mailto_unknown, service[1], host))
            print "<p>Response strings for unknown service %s were:" % service[1]
            print "<ol>"
            for str in service[0].patterns.attempts:
                print "<li><tt>%s</tt>" % string.replace(str, "\n", "<br>\n")
                pipe.write(str)
                pipe.write("\n")
            print "</ol></p><hr>"
            pipe.close()

    print "</body></html>"

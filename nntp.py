from nntplib import NNTP
from patterns import PATTERNS

patterns = PATTERNS([
    (r"20\d NNTP Service Microsoft.* Internet Services \S+ Version: (\S+)",
     "Microsoft IIS"),
	(r"20\d NNTP Service \d+\.\d+\.\d+ Version: (\S+)", "Microsoft IIS?"),
    (r"20\d \S+ InterNetNews NNRP server INN (\S+) \S+ ready", "INN"),
	(r"20\d \S+ InterNetNews NNRP server INN (\S+) ready", "INN"),
	(r"20\d \S+ InterNetNews NNRP server INN (\S+) \(.+\) ready", "INN"),
    (r"20\d Microsoft Exchange Internet News Service (Version \S+)",
     "Microsoft Exchange"),
    (r"20\d .* \(Typhoon (v\S+)\)", "Typhoon"),
    (r"20\d Supernews NNRP server ready - http://www.supernews.com",
     "Supernews custom"),
    (r" Netscape-News/([^\s]+)", "Netscape News"),
    (r" Netscape-News", "Netscape News"),
	(r"20\d \S+ Netscape-Collabra/(\S+) \S+ NNRP ready", "Netscape Collabra"),
    (r" Lotus Domino NNTP Server for \S+ \((Release .*)\)", "Lotus Domino"),
    (r" Leafnode NNTP Daemon, version (\S+) running", "Leafnode"),
    (r" newsfeeds DNEWS Version ([^,]+),", "DNews"),
    ])

def identify(host):
    h = NNTP(host)
    w = h.getwelcome()
    h.quit()
    return patterns.match(w)

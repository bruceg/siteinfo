from nntplib import NNTP
from patterns import PATTERNS

patterns = PATTERNS([
    (r"20\d \S+ InterNetNews NNRP server INN (\S+) \S+ ready", "INN"),
    (r"20\d Microsoft Exchange Internet News Service (Version \S+)",
     "Microsoft Exchange"),
    (r"20\d .* \(Typhoon (v\S+)\)", "Typhoon"),
    (r"20\d Supernews NNRP server ready - http://www.supernews.com",
     "Supernews custom", "http://www.supernews.com/"),
    (r"Netscape-News/([^\s]+)", "Netscape News"),
    (r"Netscape-News", "Netscape News"),
    ])

def identify(host):
    h = NNTP(host)
    w = h.getwelcome()
    h.quit()
    return patterns.match(w)

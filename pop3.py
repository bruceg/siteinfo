from poplib import POP3
from patterns import PATTERNS
import re

patterns = PATTERNS([
    (r"MailSite POP3 Server (\S+) Ready", "MailSite"),
    (r"Microsoft Exchange POP3 server (version \S+) ready",
     "Microsoft Exchange"),
    (r"Cubic Circle's (v\S+) \S+ POP3 ready",
     "Cubic Circle's POP3"),
    (r"Solstice \(tm\) Internet Mail Server \(tm\) POP3 (\S+) at",
     "Solstice Internet Mail Server (Sun)"),
    (r" POP3 service \(Netscape Messaging Server (\S+) \(built .*\)\)",
     "Netscape Messaging Server"),
    (r"POP3 server \(Netscape Mail Server (v\S+)\) ready",
     "Netscape Mail Server"),
    (r"X1 NT-POP3 Server \S+ \(IMail (\S+ \S+)\)",
     "IMail"),
    (r"CommuniGate Pro POP3 Server (\S+) ready",
     "CommuniGate Pro"),
    (r"running Eudora Internet Mail Server (\S+)",
     "Eudora Internet Mail Server"),
    (r"POP3 server \(Post.Office (v\S+ release \S+.*)\) ready",
     "InterMail Post.Office Edition"),
    (r"QPOP \((version .+)\) at .+ starting",
     "Qualcomm qpopper"),
    (r"QPOP \((version .+)\)",
     "Qualcomm qpopper"),
    (r"MercuryP/NLM (v.+) ready",
     "MercuryP/NLM"),
    (r"MercuryP/32 (v.+) ready",
     "Mercury/32"),
    (r"MercuryP/32", "Mercury/32"),
    (r"OK VOPmail POP3 Server (\S+) Ready", "VOPmail"),
    (r" POP3 service ready \[\d+\] \(MDaemon (v.+)\)$", "MDaemon"),
    (r" Cyrus POP3 (v\S+) server ready$", "Cyrus"),
    (r"^$",
     "No identification strings, possibly qmail")
    ])

def strip(string):
    rx = re.compile(r"^\+OK\s+<[^>]+>\s*")
    m = rx.match(string)
    if m:
        return string[m.end():]
    else:
        return string

def identify(host):
    h = POP3(host)
    w = strip(h.getwelcome())
    h.quit()
    return patterns.match(w)

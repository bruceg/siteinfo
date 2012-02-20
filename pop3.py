from poplib import POP3
from patterns import PATTERNS
import re

patterns = PATTERNS([
    (r"MailSite POP3 Server (\S+) Ready", "MailSite"),
    (r"Microsoft Exchange POP3 server (version \S+) ready",
     "Microsoft Exchange"),
    (r"Microsoft Exchange \d+ POP3 server (version \S+) ready",
     "Microsoft Exchange"),
	(r"Microsoft Exchange Server \d+ POP3 server (version \S+) ",
	 "Microsoft Exchange"),
    (r"Cubic Circle's (v\S+) \S+ POP3 ready",
     "Cubic Circle's POP3"),
    (r"Solstice \(tm\) Internet Mail Server \(tm\) POP3 (\S+) at",
     "Solstice Internet Mail Server (Sun)"),
    (r" POP3 service \(Netscape Messaging Server (\S+ Patch \S+) \(built .*\)\)",
     "Netscape Messaging Server"),
    (r" POP3 service \(Netscape Messaging Server (\S+) \(built .*\)\)",
     "Netscape Messaging Server"),
    (r" POP3 server \(Netscape Messaging Server - Version (\S+)\) ready",
     "Netscape Messaging Server"),
    (r"POP3 server \(Netscape Mail Server (v\S+)\) ready",
     "Netscape Mail Server"),
    (r"X1 NT-POP3 Server \S+ \(IMail (\S+ \S+)\)", "IMail"),
    (r"CommuniGate Pro POP3 Server (\S+) ready", "CommuniGate Pro"),
    (r"OK CommuniGate POP is ready. (V\S+) ", "CommuniGate"),
    (r"running Eudora Internet Mail Server (\S+)",
     "Eudora Internet Mail Server"),
    (r"POP3 server \(Post.Office (v\S+ release \S+.*)\) ready",
     "InterMail Post.Office Edition"),
    (r"QPOP \((version .+)\) at .+ starting", "Qualcomm Qpopper"),
    (r"QPOP \((version .+)\)", "Qualcomm Qpopper"),
    (r"Qpopper \((version .+)\)", "Quallcomm Qpopper"),
    (r"MercuryP/NLM (v.+) ready", "MercuryP/NLM"),
    (r"MercuryP/32 (v.+) ready", "Mercury/32"),
    (r"MercuryP/32", "Mercury/32"),
    (r"OK VOPmail POP3 Server (\S+) Ready", "VOPmail"),
    (r" POP3 service ready \[\d+\] \(MDaemon (v.+)\)$", "MDaemon"),
    (r" MDaemon (\S+) MDaemon", "MDaemon"),
    (r" Cyrus POP3 (v\S+) server ready$", "Cyrus"),
    (r" Lotus Notes POP3 server version (\S+) ready", "Lotus Domino"),
    (r" Stalker POP3 Server (\S+) at \s+ ready", "SIMS"),
    (r"OK POP3 server ready \(NPlex (\S+)\)", "NPlex"),
	(r"OK [Dd]ovecot ready", "Dovecot"),
	(r"OK POP3 \S+ (v2\d\d\d\.\d+) server ready", "imap-uw"),
	(r"OK \S+ \(POP-Max (Version \S+),", "MailMax"),
	(r"OK DPOP (Version \S+)\. <\S+>", "DMail"),
	(r"OK POP3 server ready \(running FTGate (V\d+, \d+, \d+),", "FTGate"),
	(r"^\+OK Hello there\.", "Courier IMAP"),
    (r"^\+OK $", "No identification strings, possibly qmail")
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

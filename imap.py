from imaplib import IMAP4
from patterns import PATTERNS

patterns = PATTERNS([
    (r"OK \S+ IMAP4 Service (\S+\(\S+\)) at .* \(Report problems in this server to MRC@CAC.Washington.EDU\)", "UWashington IMAP4?"),
    (r"OK \S+ IMAP4 Service (\S+\(\S+\)) at", "UWashington IMAP4?"),
    (r"OK \S+ Solstice \(tm\) Internet Mail Server \(tm\) IMAP4 service @ (\S+) - at", "Solstice Internet Mail Server (Sun)"),
    (r"OK \S+ IMAP4rev1 (v[\S]+) server ready", "UWashington IMAP"),
    (r"OK Microsoft Exchange IMAP4rev1 server (version \S+) \(.*\) ready",
     "Microsoft Exchange" ),
    (r"OK Netscape IMAP4 Service (\S+) on \S+ at ", "Netscape"),
    (r"OK NTMail IMAP4 server (\S+) ready", "NTMail"),
    (r"OK \S+ Cyrus IMAP4 (v\S+) server ready", "Cyrus"),
    (r"OK IMAP4 Server \(IMail (\S+)\)", "IMail"),
    (r"OK CommuniGate Pro IMAP Server (\S+) at \S+ ready", "CommuniGate Pro"),
    (r"OK OpenMail IMAP server (\S+) ready", "OpenMail"),
    ])

def identify(host):
    h = IMAP4(host)
    w = h.welcome
    b = h.logout()
    return patterns.match(w)

from ftplib import FTP
from patterns import PATTERNS

patterns = PATTERNS([
    (r"ProFTPD (\S+) Server", "ProFTPD"),
    (r"FTP server \(BSDI (Version \S+)\) ready", "BSDI FTP daemon"),
    (r"FTP server \((Version wu-\S+) .*\) ready", "wu-ftpd"),
    (r" NcFTPd Server \(unregistered copy\) ready", "NcFTPd"),
    (r" NcFTPd Server \(free personal license\) ready", "NcFTPd"),
    (r" NcFTPd Server \(licensed copy\) ready", "NcFTPd"),
    (r" Microsoft FTP Service \((Version \S+)\)", "Microsoft FTP"),
    (r"^220.Serv-U FTP-Server (v\S+) for WinSock ready", "Serv-U FTP"),
    (r"^220.Serv-U FTP-Server (v\S+ build \S+) for WinSock ready",
     "Serv-U FTP"),
    (r"^214 Serv-U (version \S+), registered to: ", "Serv-U FTP"),
    (r"^214 Serv-U, registered to: ", "Serv-U FTP"),
    (r" FTP server \(NcFTPd (\S+)\) ready", "NcFTPd"),
    (r" WarFTPd (\S+) \(.*\) Ready", "WarFTPd"),
    ])

def identify(host):
    h = FTP(host)
    w = h.getwelcome()
    help = h.sendcmd("HELP")
    h.quit()
    return patterns.match(w) or \
           patterns.match(help)

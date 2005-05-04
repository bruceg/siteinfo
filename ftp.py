from ftplib import FTP, error_perm
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
    (r" NetPresenz (v\S+) awaits your command", "NetPresenz"),
    (r"^214 Send server bug reports to <support@stairways.com.au>.",
     "NetPresenz"),
    (r"^220 \S+ FTP server \(NcFTPd (.+)\) ready", "NcFTPd"),
    (r"^214 publicfile ", "publicfile"),
	(r"^220[- ]TwoFTPd server ready", "TwoFTPd"),
	(r"^220 Authenticate first", "TwoFTPd"),
	(r"^200 Awaiting your commands, master\.\.\.", "TwoFTPd"),
	(r"^502 No help is available\.", "TwoFTPd"),
	(r"\(vsFTPd (\S+)\)", "vsftpd"),
	(r"You're talking to vsftpd.", "vsftpd"),
    ])

def identify(host):
	h = FTP(host)
	w = h.getwelcome()
	try: nocmd = h.sendcmd("TESTING")
	except error_perm, nocmd: pass
	try: noop = h.sendcmd("NOOP")
	except error_perm, noop: pass
	try: help = h.sendcmd("HELP")
	except error_perm, help: pass
	h.quit()
	return patterns.match(w) or \
		   patterns.match(nocmd) or \
		   patterns.match(noop) or \
		   patterns.match(help)

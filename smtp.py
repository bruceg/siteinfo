import smtplib
from patterns import PATTERNS

class SMTP(smtplib.SMTP):
    def __init__(self, host=None):
        smtplib.SMTP.__init__(self,host)
    def docmd(self,cmd,args=""):
        self.putcmd(cmd,args)
        (code,msg) = self.getreply()
        return msg

patterns = PATTERNS([
    (r" InterScan VirusWall NT ESMTP (\S+) ", "InterScan VirusWall"),
    (r" ESMTP server \(InterMail (v\S+).*\) ready", "InterMail"),
    (r"This SMTP server is a part of the InterMail E-mail system.", "InterMail"),
    (r"information about InterMail, please see ", "InterMail"),
    (r" ESMTP Service \(Lotus Domino (Release \S+).*\) ready", "Lotus Domino"),
    (r"Sorry, you are not authorized to make this connection", "Raptor proxy"),
    (r"Server ESMTP \(Sun Internet Mail Server sims\.(.+)\)",
     "Solstice Internet Mail Server (Sun)"),
    (r"Sun Internet Mail Server", "Solstice Internet Mail Server (Sun)"),
    (r"Sorry, unable to contact destination SMTP daemon", "Raptor proxy"),
    (r"MERCUR SMTP-Server .v.* for Windows NT ready at", "MERCUR"),
    (r"MERCUR SMTP-Server .v.* for Windows 95 ready at", "MERCUR"),
    (r"forging of mail requires recognizable SMTP", "unknown (requires recognizable SMTP)"),
    (r" ESMTP service ready .* \(MDaemon ([^\)]+)\)", "MDaemon"),
    (r"MDaemon .* Help system currently inactive", "MDaemon"),
    (r"Microsoft Exchange Internet Mail Connector", "MS Exchange"),
    (r"Microsoft Exchange Internet Mail Service", "MS Exchange"),
    (r" Microsoft ESMTP MAIL Service, (Version: \S+) ready", "MS Exchange?"),
    (r"CheckPoint FireWall-1 secure SMTP server", "CheckPoint firewall"),
    (r"Stalker Internet Mail Server .*is ready", "Stalker"),
    (r"NT Server running Internet Shopper", "NT Mail"),
    (r"Simple Mail Transfer Service Ready", "unknown (Simple Mail Transfer Service Ready)"),
    (r"http:..pobox.com..djb.qmail.html", "qmail"),
    (r"send comments to qmail@pobox.com", "qmail"),
    (r"unable to read controls..#4.3.0", "qmail"),
    (r"unimplemented..#5.5.1", "qmail"),
	(r"Sorry, that domain isn't in my list of allowed rcpthosts.", "qmail"),
    (r"Mercury 1\... ESMTP server ready", "Mercury"),
    (r"Mercury 1\... SMTP server ready", "Mercury"),
    (r"PC.TCP SMTPSRV by FTP Software", "PC/TCP SMTPSRV"),
    (r"VOPMail ESMTP Receiver Version (\S+) Ready", "VOPMail"),
    (r"VOPMail SMTP Receiver Version (\S+) Ready", "VOPMail"),
    (r"VOPMail ESMTP Receiver Version ", "VOPMail"),
    (r"VOPMail SMTP Receiver Version ", "VOPMail"),
    (r"Running on The Major BBS with ", "Major BBS"),
    (r" ESMTP .IPAD 2....... ready at", "IPAD"),
    (r"CommuniGate SMTPGate is ready", "CommuniGate SMTP"),
    (r"ESMTP CommuniGate Pro (\S+).", "CommuniGate Pro ESMTP"),
    (r"bugs to The Wollongong Group", "Wollongong SMTP"),
    (r"Microsoft SMTP MAIL ready at", "Microsoft SMTP MAIL"),
    (r"Eureka! Gold Internet Server", "Eureka! Gold Internet Server"),
    (r"Eudora Internet Mail Server", "Eudora Internet Mail Server, formerly AIMS, formerly MailShare"),
    (r" ESMTP .IPAD 2.... ready at", "IPAD"),
    (r"Apple Internet Mail Server", "Eudora Internet Mail Server, formerly AIMS, formerly MailShare"),
    (r" GroupWise Internet Agent ", "Groupwise Internet Agent"),
    (r" ESMTP .IPAD 2... ready at", "IPAD"),
    (r" ESMTP .IPAD 1... ready at", "IPAD"),
    (r"Ready for business. iSMTP", "iSMTP"),
    (r"post.office E-mail system", "Post.Office"),
    (r"Mercury SMTP server ready", "Mercury"),
    (r"CommuniGate SMTP is ready", "CommuniGate SMTP"),
    (r"Netscape Messaging Server (\S+ Patch \S+)", "Netscape Messaging Server, formerly Netscape Mail Server"),
    (r"Netscape Messaging Server", "Netscape Messaging Server, formerly Netscape Mail Server"),
    (r"ESMTP Service .Worldmail ", "Worldmail"),
    (r"ESMTP Service .WorldMail ", "Worldmail"),
    (r"TGV.MultiNet SMTP server", "CISCO MultiNet, formerly TGV/MultiNet"),
    (r"Sun Internet Mail Server", "Solstice Internet Mail Server (Sun)"),
    (r"running IBM AS.400 SMTP", "AS/400 SMTP"),
    (r"Mail.Link  SMTP Package", "Mail*Link"),
    (r"FirstClass Mail Server ", "FirstClass"),
    (r"This is Fwmail version ", "Fwmail"),
    (r"NetManage SMTP service", "NetManage SMTP service"),
    (r"MailSite ESMTP Receiver Version (\S+) Ready", "MailSite"),
    (r"MailSite SMTP Receiver Version (\S+) Ready", "MailSite"),
    (r"MailSite ESMTP Receiver", "MailSite"),
    (r"MailSite SMTP Receiver", "MailSite"),
    (r"Worldgroup SMTP server", "Worldgroup SMTP server"),
    (r"Duhmail..Black Hole v", "sendmail# *.sid.ncr.doe.ca"),
    (r"ESMTP Service .NPlex ", "NPlex"),
    (r"Generic SMTP handler", "Raptor firewall"),
    (r"Netscape Mail Server", "Netscape Messaging Server, formerly Netscape Mail Server"),
	(r"^\S+ mailfront ESMTP", "mailfront"),
    (r" SMTP Server SLmail ", "SLmail"),
    (r"EMWAC SMTP Receiver", "EMWAC SMTP Receiver"),
    (r"GroupWise SMTP.MIME", "GroupWise"),
    (r"Sendmail (.+) ready", "sendmail"),
    (r"Mercury/32 (v[^ ]+)", "Mercury/32"),
    (r"MetaInfo Sendmail", "MetaInfo Sendmail, port of sendmail to NT"),
    (r"IMS SMTP Receiver", "IMS SMTP Receiver"),
    (r"running MailShare", "Eudora Internet Mail Server, formerly AIMS, formerly MailShare"),
    (r"ListSTAR Package", "ListSTAR"),
    (r"TGV MultiNet V", "CISCO MultiNet, formerly TGV/MultiNet"),
    (r"AltaVista Mail", "AltaVista Mail"),
    (r"MindWire-SMTP ", "MindWire-SMTP"),
    (r"Lotus SMTP MTA", "Lotus SMTP MTA"),
    (r"MX V.\..-. VAX", "VMS MX"),
    (r"\(PMDF#..... V", "PMDF"),
    (r"ESMTP VMailer", "VMailer"),
    (r"Error: send HELO/EHLO first$", "Postfix"),
    (r"Error: need MAIL command$", "Postfix"),
    (r"ESMTP Postfix", "Postfix"),
    (r"post.office v", "Post.Office"),
    (r"Connect2-SMTP", "Connect2-SMTP"),
    (r" SMTP \(PMDF ", "PMDF"),
    (r"Sendmail (.+);", "sendmail"),
    (r"MX V.\.. VAX", "VMS MX"),
    (r"TFS Gateway ", "TFS Gateway"),
    (r"MX V.\.. AXP", "VMS MX"),
    (r"Zachariassen", "Zmailer"),
    (r"Pony Express", "Pony Express"),
    (r"SMTP.OpenVMS", "SMTP-OpenVMS"),
    (r" Smail ready", "Smail"),
    (r"IBM VM SMTP", "IBM VM SMTP"),
    (r" IMA SMTP ", "IMA SMTP"),
    (r"NASTA Gate", "NASTA Gate"),
    (r"Mercury/32", "Mercury/32"),
    (r"SMTP.smap", "smap"),
    (r"Smail-3.2", "Smail"),
    (r"Smail 3.1", "Smail"),
    (r"smail 3.1", "Smail"),
    (r"Smail3.2", "Smail"),
    (r"Smail3.1", "Smail"),
    (r"SLmail95", "SLmail"),
    (r"SLmailNT", "SLmail"),
    (r"SLMAILNT", "SLmail"),
    (r"Sendmail", "sendmail"),
    (r"PMDF V", "PMDF"),
    (r"SMTPXD", "AltaVista firewall"),
    (r"IMail", "IMail"),
    (r"Exim", "Exim"),
    (r"UCX ", "UCX"),
    (r"[pP][pP].*Pleased to meet you", "PP"),
    (r"Help \.\.\. Not recognized", "unknown (Help ... Not recognized)"),
    (r"HELP \.\.\. Not recognized", "unknown (Help ... Not recognized)"),
    (r"For more info use .HELP", "sendmail"),
    (r" All set, fire away", "MSMail SMTP gateway"),
    (r"Complaints.bugs to", "MMDF"),
	(r"\S+ \(Mail-Max (Version \S+),", "MailMax"),
	(r"Welcome to Mail-Max (v\S+)", "MailMax"),
	(r"\S+ DSMTP ESMTP Server (v\S+)", "DMail"),
	(r"Help for DSMTP (v\S+)", "DMail"),
	(r"\S+ ESMTP Lyris service ready", "Lyris"),
	(r"User unknown to Lyris List Manager", "Lyris"),
	(r"SMTP/cmap ready", "Cisco PIX Firewall SMTP Proxy v4.x"),
    ])

def identify(host):
	connection = SMTP()
	(code,resp) = connection.connect(host)
	return patterns.match(resp) or \
           patterns.match(connection.docmd('help')) or \
           patterns.match(connection.docmd('xxxx')) or \
           patterns.match(connection.docmd('mail from:<nobody@nowhere.net>')) or \
           patterns.match(connection.docmd('rcpt to:<nobody@nowhere.net>'))

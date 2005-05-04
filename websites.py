websites = {
	'InterMail': 'http://www.software.com/',
	'MailSite': 'http://www.mailsite.com/',
	'qmail': 'http://www.qmail.org/',
	'Supernews custom': 'http://www.supernews.com/',
	'Supernews': 'http://www.supernews.com/',
	'wu-ftpd': 'http://www.wu-ftpd.org/',
	'NetPresenz': 'http://www.stairways.com/netpresenz/',
	'Lotus Domino': 'http://www.lotus.com/home.nsf/welcome/domino',
	'SIMS': 'http://www.stalker.com/SIMS/',
	'Leafnode': 'http://www.leafnode.org/',
	'OpenMail': 'http://www.hp.com/go/openmail',
	'NcFTPd': 'http://www.ncftpd.com/ncftpd/',
	'publicfile': 'http://cr.yp.to/publicfile.html',
	'Courier IMAP': 'http://www.courier-mta.org/imap/',
	'Courier': 'http://www.courier-mta.org/',
	'mailfront': 'http://untroubled.org/mailfront/',
	'DNews': 'http://netwinsite.com/dnews.htm',
	'Twister': 'http://www.nntpd.com/twister.shtml',
	'Microsoft Exchange': 'http://www.microsoft.com/exchange/',
	'TwoFTPd': 'http://untroubled.org/twoftpd/',
	'Binc IMAP': 'http://www.bincimap.org/',
	'vsftpd': 'http://vsftpd.beasts.org/',
}

def find(name):
	return websites.get(name, None)

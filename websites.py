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
	'Courier IMAP': 'http://www.inter7.com/courierimap',
	'Courier': 'http://www.courier-mta.org/',
}

def find(name):
	return websites.get(name, None)

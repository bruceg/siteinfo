websites = {
	'InterMail': 'http://www.software.com/',
	'MailSite': 'http://www.mailsite.com/',
	'qmail': 'http://www.qmail.org/',
	'Supernews custom': 'http://www.supernews.com/',
	'Supernews': 'http://www.supernews.com/',
	'wu-ftpd': 'http://www.wu-ftpd.org/',
	'NetPresenz': 'http://www.stairways.com/netpresenz/',
	'Lotus Domino': 'http://www.lotus.com/home.nsf/welcome/domino',
}

def find(name):
	return websites.get(name, None)

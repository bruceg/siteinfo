websites = {
	"InterMail": "http://www.software.com/",
	"qmail": "http://www.qmail.org/",
	"MailSite": "http://www.mailsite.com/",
	"wu-ftpd": "http://www.wu-ftpd.org/",
}

def find(name):
	return websites.get(name, None)

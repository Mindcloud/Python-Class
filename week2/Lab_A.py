import urllib2

def firstpart():
	response = urllib2.urlopen('http://briandorsey.info/uwpython/week01/email_vm.py')
	html = response.read()
	fp = open('email_vm.py', 'w')

	for line in html:
		fp.write(line)
		
	fp.close

def processHtmlFile(fName):
	fp = open(fName, 'r')
	i = 0
	for line in fp:
		print 'Processing....' + line
		response = urllib2.urlopen(line)
		html = response.read()
		sFile = 'File' + str(i) + '.txt'
		fpNew = open(sFile, 'w')
		for line in html:
			fpNew.write(line)
		fpNew.close()
		i = i + 1
	fp.close()

processHtmlFile('urls.txt')
#firstpart()

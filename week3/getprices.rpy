#This script grabs my items from a google spreadsheet here
# https://spreadsheets.google.com/ccc?key=0AuxijFHrtipddEx0SjdTMUR0Uld3YTc2LU9ORGRZRWc&hl=en&authkey=CLy6Ow
#
# It parses the items and grabs the price from Amazon and generates a basic web page with the results here
# http://208.85.148.174:8080/getprices.rpy
# TODO: Be smart about which price, maybe grab the lowest amount or something
# Also the page needs better formatting, but it took me many hours of trial and error to get this much

# Note: I stripped all the keys out of the code, but if you go to the web site, I used twisted to host it

from twisted.web.resource import Resource 
from twisted.web import server 
from twisted.internet import utils 
from twisted.python import util
try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
import getopt
import sys
import string
from amazonproduct import API

class Ssheet:

	def __init__(self):
		self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
		self.gd_client.email = 'xxxxxxxxx@gmail.com'
		self.gd_client.password = 'XXXXXXX'
		self.gd_client.source = 'Spreadsheets GData Sample'
		self.gd_client.ProgrammaticLogin()
		#self.curr_key = ''
		self.curr_key = ''
		self.curr_wksht_id = ''
		self.feed = None

 	def _GetCellFeed(self):
		self.feed = self.gd_client.GetCellsFeed(self.curr_key, self.curr_wksht_id)

    #this does not work for some reason, always gives me a 400
	def _UpdateCell(self, row, col, inputValue):
		entry = self.gd_client.UpdateCell(row=row, col=col, inputValue=inputValue, 
			key=self.curr_key, wksht_id=self.curr_wksht_id)
  
	def _ShowPrices(self, feed):
		prices = []
		for item in feed.entry:
			prices.append(item.content.text)
			print item.content.text
		return prices

	def Run(self):
		self._GetCellFeed()
		return self._ShowPrices(self.feed)

	def _GetPrice(self, srchStr):
		api = API('XXXXXXX','XXXXXX', 'us')
		node = api.item_search('Electronics',Keywords=srchStr, ResponseGroup='ItemAttributes' )
		firstitem = node.Items.Item
		itemprice = firstitem.ItemAttributes.ListPrice.FormattedPrice
		print itemprice
		return itemprice

class PriceResource(Resource):

	def render_GET(self, request):
		isLeaf = True
		prices = Ssheet()
		pList = prices.Run()
		print pList
		pListOut = ''
		for line in pList:
			itemprice = prices._GetPrice(line)
			pListOut = pListOut + line + ' ' + itemprice + '<br>'
		return "<html><body>%s</body></html>" % (pListOut,)

resource = PriceResource()


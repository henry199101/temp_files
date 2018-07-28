import http.client
import json
from urllib.parse import quote_plus

base = '.maps/api/geocode/json'

def geocode(address):
	path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
	connection = http.client.HTTPConnection('maps.googleapis.com')
	connection.requests('GET', path)
	rawreply = connnection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
	geocode('207 N. Defiance St, Archbold, OH')

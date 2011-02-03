from cgi import parse_qs, escape
import json,time

def application(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'a' in parameters:
        intA = escape(parameters['a'][0])
    else:
        return 'Missing a in parameters'
    if 'b' in parameters:
	intB = escape(parameters['b'][0])
    else:
	return 'Missing b in parameters'
    start_response('200 OK', [('Content-Type', 'text/plain')])
    total = int(intA) + int(intB)
    #return ['''Hello %(subject)s
    #''' % {'subject': subject}]
    return json.dumps({"result":total,"uwnetid":"mcloudx","time":time.time()}, indent=4, sort_keys=False)


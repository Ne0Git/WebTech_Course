def app(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [bytes(env['QUERY_STRING'].replace('&', '\n'), 'utf-8')]

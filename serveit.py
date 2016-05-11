#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import argparse

DEFAULT_PORT = 8080

def run(port):
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", port), Handler)

	print "new serving at port", port
	print "CTRL+C to stop server"

	httpd.serve_forever()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='A very simple webserver for your RWD goodness')
	parser.add_argument('-p', '--port', help='port to serve on', type=int)
	args = parser.parse_args()

	if args.port:
		run(args.port)
	else:
		run(DEFAULT_PORT)

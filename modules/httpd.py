# httpd.py
#
# Custom thread class for handling HTTP requests

import BaseHTTPServer
import SimpleHTTPServer
import SocketServer


# A thread class for handling HTTP requests
#
class HTTPServerThread (threading.Thread):

	# the port on which to serve requests
	#
	port = 8080

	# the handler class
	#
	handlerClass = None

	# the server class
	#
	serverClass = None

	# the instantiated HTTP daemon
	#
	httpd = None

	# initialize the server
	#
	def __init__(self, port=8080):
		threading.Thread.__init__(self)

		self.port         = port
		self.handlerClass = SimpleHTTPServer.SimpleHTTPRequestHandler
		self.serverClass  = BaseHTTPServer.HTTPServer

		protocol     = "HTTP/1.0"

		server_address = ('127.0.0.1', self.port)
		self.handlerClass.protocol_version = protocol

		self.httpd = self.serverClass(server_address, self.handlerClass)


	# run the server
	#
	def run(self):
		# the main loop for the HTTP server
		#
		sa = self.httpd.socket.getsockname()
		print "Serving HTTP on", sa[0], "port", sa[1], "..."
		self.httpd.serve_forever()


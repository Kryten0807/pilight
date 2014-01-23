# httpd.py
#
# Custom thread class for handling HTTP requests

import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import re
import urllib


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
		self.handlerClass = piRequestHandler
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



# the pilight
class piRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	rgx = None

	# override the handler for GET requests
	#
	def do_GET(self):
		# has the regex object been compiled yet? if not, do it now
		#
		if self.rgx == None:
			self.rgx = re.compile('^\/(\?speech\=(.*))?$')

		# check the path
		#
		m = self.rgx.search(self.path)

		# did we get a match? if so, parse the results
		#
		speech = None

		if m:
			# did we get a match to the parameters part of the URL
			if m.group(2):
				speech = urllib.unquote_plus(m.group(2))

		# did we get a match? if so, act on it
		#
		if m:

			self.wfile.write(
				"""
<html>
	<head>
	</head>

	<body>
		<h1>Enter the text string:</h1>
		<form action="/" method="GET">
			<input type="text" name="speech" placeholder="Enter something to say" />
			<button type="submit">Say it!</button>
		</form>

				"""
				)

			if speech:
				self.wfile.write("<h2>Saying...</h2>")
				self.wfile.write("<pre>")
				self.wfile.write(speech)
				self.wfile.write("</pre>")

			self.wfile.write(
				"""
	</body>
</html>

				"""
				)

			# speak the text string
			#
			say(speech)

			# and return
			#
			return


		# unrecognized request? pass it to the parent
		#
		self.wfile.write("<pre>")
		self.wfile.write(self.path)
		self.wfile.write("</pre>")
		# SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
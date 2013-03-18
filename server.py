""" JsonRPC server for codehero-xctr """

import web

urls = (
	'/test', 'test'
)

class test:
	def GET(self):
		return "Hola mundo!"
	def POST(self):
		return web.data()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
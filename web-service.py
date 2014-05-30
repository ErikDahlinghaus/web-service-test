#! /usr/bin/env python

import web

urls = (
	'/', 'index',
	'/create', 'create',
	'/read', 'read',
	'/update', 'update',
	'/delete', 'delete'
)

database = []

class index:
	def GET(self):
		return "This endpoint does nothing"
		

class create:
	def GET(self):
		self.POST()

	def POST(self):
		data = web.input()
		
		global database
		database.extend(data['values'].split(','))
		
		return str(database)


class read:
	def GET(self):
		global database
		return str(database)


class update:
	def GET(self):
		self.PUT()

	def PUT(self):
		data = web.input()
		
		oldvalue = data['value']
		newvalue = data['newvalue']
		
		global database
		for n,i in enumerate(database):
			if i == oldvalue:
				database[n] = newvalue
		

class delete:
	def GET(self):
		self.DELETE()
	
	def DELETE(self):
		data = web.input()
		
		value = data['value']
		
		global database
		for n,i in enumerate(database):
			if i == value:
				database.pop(n)
		

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
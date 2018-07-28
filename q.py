class A():
	def __init__(self):
		pass
	def __iter__(self):
		yield 1
		print 1

a = A()
a.__iter__()


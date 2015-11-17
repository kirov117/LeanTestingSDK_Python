#!/usr/bin/env python

# import tst

print('MAIN')


class MyOBJ:
	_field = 'Nebellwerfer'
	data = 'works...'

class MyWOW(MyOBJ):

	def __init__(self):
		print(self._field)

a = MyWOW()

# class dynClass:

# 	def __init__(self, cls):
# 		new = cls()
# 		print(type(new))

# a = dynClass(MyOBJ)

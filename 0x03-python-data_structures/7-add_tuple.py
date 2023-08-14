#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	a = tuple_a[:2]
	b = tuple_b[:2]

	if len(a) < 2:
		a += (0,) * (2 - len(a))
	if len(b) < 2:
		b += (0,) * (2 - len(b))

	a1, a2 = a
	b1, b2 = b

	result = (a1 + b1, a2 + b2)
	return result

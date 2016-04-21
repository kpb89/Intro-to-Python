Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> line1 = "a1, m1, m2, m3"
>>> line2 = "a2, m1, m2, m3"
>>> line1 = line1.strip()
>>> line1
'a1, m1, m2, m3'
>>> line2 = line2.strip()
>>> line2
'a2, m1, m2, m3'
>>> entry1 = line1.split(',')
>>> entry1
['a1', ' m1', ' m2', ' m3']
>>> entry2 = line2.split(',')
>>> entry2
['a2', ' m1', ' m2', ' m3']
>>> actordata = {}
>>> actordata[entry1[0]] = entry1[1:]
>>> actordata
{'a1': [' m1', ' m2', ' m3']}
>>> actordata[entry2[0]] = entry2[1:]
>>> actordata
{'a2': [' m1', ' m2', ' m3'], 'a1': [' m1', ' m2', ' m3']}
>>> print('**All actors in the database:')
**All actors in the database:
>>> for a in actordata:
	return [0]
SyntaxError: 'return' outside function
>>> for a in actordata:
	

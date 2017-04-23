class Tsunderesult(object):
	def __init__(self, result, response):
		self.result = result
		self.response = response
		
	def is_successful(self):
		return self.result
		
	def get_response(self):
		return None if not self.result else self.response

def tsundere(s):
	if not isinstance(s, str):
		print("not even a string")
		return Tsunderesult(False, None)
	
	if not (s[0].isalpha() and s[0].isupper()):
		print("sentence does not begin with a capitalized letter")
		return Tsunderesult(False, None)
	
	if (s[-1] != "."):
		print("sentence does not end with a period")
		return Tsunderesult(False, None)
		
	# remove period
	s = s[:-1]
	
	# un-capitalize the first letter, unless it's the 1st singular personal pronoun "I"
	if (s[0:2] != "I "):
		t = s[1:]
		s = s[0].lower() + t
	
	return Tsunderesult(True, "I-It's not like " + s + ", baka!!!")

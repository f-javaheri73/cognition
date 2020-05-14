Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class time:
    def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.secoud = s
    def __init__(obj1,h,m,s):
        obj1.hour = h
        obj1.minute = m
        obj1.second = s
# a method for calculating total seconds 
    def total_s(obj):
        return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
    def add(obj, h1,m1,s1):
        return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
    def mix(obj,obj1):
        s_more =obj.second + obj1.second
        m_more = obj.minute+obj1.minute
        h_total = obj.hour+obj1.hour
        if s_more >60:
            m_more += s_more // 60
            s_more  = s_more %60
        if m_more >60:
            h_total += m_more //60
            m_more = m_more % 60
        return (h_total),(m_more),(s_more)

>>> def __sub__(obj,obj1):
	s_less = obj.second - obj1.second
	m_less = obj.minute - obj1.minute
	h_less = obj.hour - obj1.hour
	if s_less <0:
		s_less = obj1.second - obj.second
	if m_less <0:
		m_less = obj1.minute - obj.minute
	if h_less <0:
		h_less = obj1.hour - obj.hour
	return str(h_less)+':'+ str(m_less)+':'+str(s_less)

>>> 
>>> t1 = time()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t1 = time()
TypeError: __init__() missing 3 required positional arguments: 'h', 'm', and 's'
>>> t1 = time(3,40,12)
>>> t2 = time(2,30,10)
>>> t2 - t1
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t2 - t1
TypeError: unsupported operand type(s) for -: 'time' and 'time'
>>> class time:
	
	def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.secoud = s
	def __init__(obj1,h,m,s):
        obj1.hour = h
        obj1.minute = m
        obj1.second = s
# a method for calculating total seconds
	def total_s(obj):
		return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
	 def add(obj, h1,m1,s1):
		return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
	def mix(obj,obj1):
		
		s_more =obj.second + obj1.second
		m_more = obj.minute+obj1.minute
		h_total = obj.hour+obj1.hour
		if s_more >60:
		m_more += s_more // 60
		s_more  = s_more %60
		if m_more >60:
		h_total += m_more //60
		m_more = m_more % 60
		return (h_total),(m_more),(s_more)
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class time:

	def __init__(obj,h,m,s):
		
		obj.hour = h
		obj.minute = m
		obj.secoud = s
	def __init__(obj1,h,m,s):
		obj1.hour = h
		obj1.minute = m
		obj1.second = s
# a method for calculating total seconds
	def total_s(obj):
		return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
	 def add(obj, h1,m1,s1):
		return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
	def mix(obj,obj1):

		s_more =obj.second + obj1.second
		m_more = obj.minute+obj1.minute
		h_total = obj.hour+obj1.hour
		if s_more >60:
		m_more += s_more // 60
		s_more  = s_more %60
		if m_more >60:
		h_total += m_more //60
		m_more = m_more % 60
		return (h_total),(m_more),(s_more)
	
SyntaxError: unindent does not match any outer indentation level
>>> class time:

	def __init__(obj,h,m,s):

		obj.hour = h
		obj.minute = m
		obj.secoud = s
	def __init__(obj1,h,m,s):
		obj1.hour = h
		obj1.minute = m
		obj1.second = s
# a method for calculating total seconds
	 def total_s(obj):
		 
		 return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
	 def add(obj, h1,m1,s1):
		 
		 return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
	def mix(obj,obj1):
		

		s_more =obj.second + obj1.second
		m_more = obj.minute+obj1.minute
		h_total = obj.hour+obj1.hour
		if s_more >60:
		m_more += s_more // 60
		s_more  = s_more %60
		if m_more >60:
		h_total += m_more //60
		m_more = m_more % 60
		return (h_total),(m_more),(s_more)
	
SyntaxError: unindent does not match any outer indentation level
>>> class time:

	def __init__(obj,h,m,s):

		obj.hour = h
		obj.minute = m
		obj.secoud = s
	def __init__(obj1,h,m,s):
		obj1.hour = h
		obj1.minute = m
		obj1.second = s
# a method for calculating total seconds
	def total_s(obj):
		return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
	def add(obj, h1,m1,s1):
		return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
	def mix(obj,obj1):

		s_more =obj.second + obj1.second
		m_more = obj.minute+obj1.minute
		h_total = obj.hour+obj1.hour
		if s_more >60:
		m_more += s_more // 60
		s_more  = s_more %60
		if m_more >60:
		h_total += m_more //60
		m_more = m_more % 60
		return (h_total),(m_more),(s_more)
	
SyntaxError: expected an indented block
>>> class time:

	def __init__(obj,h,m,s):

		obj.hour = h
		obj.minute = m
		obj.secoud = s
	def __init__(obj1,h,m,s):
		obj1.hour = h
		obj1.minute = m
		obj1.second = s
# a method for calculating total seconds
	def total_s(obj):
		return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
	def add(obj, h1,m1,s1):
		return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
	def mix(obj,obj1):

		s_more =obj.second + obj1.second
		m_more = obj.minute+obj1.minute
		h_total = obj.hour+obj1.hour
		if s_more >60:
		m_more += s_more // 60
		s_more  = s_more %60
		if m_more >60:
		h_total += m_more //60
		m_more = m_more % 60
		return (h_total),(m_more),(s_more)
	
SyntaxError: expected an indented block
>>> class time:

	def __init__(obj,h,m,s):

		obj.hour = h
		obj.minute = m
		obj.secoud = s
	def __init__(obj1,h,m,s):
		obj1.hour = h
		obj1.minute = m
		obj1.second = s
# a method for calculating total seconds
	def total_s(obj):
		return (obj.hour*3600 + obj.minute*60 +obj.secoud)
#  a method for adding new value to current time
	def add(obj, h1,m1,s1):
		return (obj.hour+h1),(obj.minute+m1),(obj.secoud+s1)
# a method for suming two instances of time class
	def mix(obj,obj1):

		s_more =obj.second + obj1.second
		m_more = obj.minute+obj1.minute
		h_total = obj.hour+obj1.hour
		if s_more >60:
		m_more += s_more // 60
		s_more  = s_more %60
		if m_more >60:
		h_total += m_more //60
		m_more = m_more % 60
		return (h_total),(m_more),(s_more)
	def __sub__(obj,obj1):
		s_less = obj.second - obj1.second
		m_less = obj.minute - obj1.minute
		h_less = obj.hour - obj1.hour
		if s_less <0:
			
			s_less = obj1.second - obj.second
		if m_less <0:
			m_less = obj1.minute - obj.minute
		if h_less <0:
			h_less = obj1.hour - obj.hour
		return str(h_less)+':'+ str(m_less)+':'+str(s_less)
	
SyntaxError: expected an indented block
>>> 

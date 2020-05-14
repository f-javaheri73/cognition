class time:
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
        return (obj.hour*3600 + obj.minute*60 +obj.second)
#  a method for adding new value to current time
    def add(obj, h1,m1,s1):
        return (obj.hour+h1),(obj.minute+m1),(obj.second+s1)
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
# defining sub, eq, lt,le,gt,ge:
    def __sub__(obj,obj1):
        s_less = obj.second - obj1.second
        m_less = obj.minute - obj1.minute
        h_less = obj.hour -obj1.hour
        if s_less <0:
            s_less = obj1.second - obj.second
        if m_less <0:
            m_less = obj1.minute - obj.minute
        if h_less <0:
            h_less = obj1.hour - obj.hour
        return str(h_less)+':'+str(m_less)+ ':'+str(s_less)
    def __eq__(obj,obj1):
        if (obj.hour*3600 + obj.minute*60 +obj.second)==(obj1.hour*3600 + obj1.minute*60 +obj1.second):
            return True
        else:
            return False
    def __lt__(obj,obj1):
        if (obj.hour*3600 + obj.minute*60 +obj.second)<(obj1.hour*3600 + obj1.minute*60 +obj1.second):
            return True
        else:
            return False
    def __le__(obj,obj1):
        if (obj.hour*3600 + obj.minute*60 +obj.second)<=(obj1.hour*3600 + obj1.minute*60 +obj1.second):
            return True
        else:
            return False
    def __gt__(obj,obj1):
        if (obj.hour*3600 + obj.minute*60 +obj.second)>(obj1.hour*3600 + obj1.minute*60 +obj1.second):
            return True
        else:
            return False
    def __ge__(obj,obj1):
        if (obj.hour*3600 + obj.minute*60 +obj.second)>=(obj1.hour*3600 + obj1.minute*60 +obj1.second):
            return True
        else:
            return False
            
    
        
        
        

            
            

        
            
        
        
    

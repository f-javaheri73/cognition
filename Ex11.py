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
            
            

        
            
        
        
    

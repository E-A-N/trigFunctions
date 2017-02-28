def degreeDepth(type ,unit):
    degrees = unit[0]
    minutes = unit[1]
    seconds = unit[2]
    newUnit = 0
    
    if type =="degree":
      for i in range(degrees):
        newUnit += 1
      return newUnit
    elif type == "minute":
      return 'minute'
    elif type == "seconds":
      return 'seconds'
      
      

def secondReduce(degree=0,minute=0,second=0):
    conversion = 0
    while degree > 0:
        minute += 60
        degree -= 1
    while minute > 0:
        second += 60
        minute -= 1
        
    conversion += second
    return conversion
    
def minuteReduce(degree=0,minute=0,second=0):
    conversion = 0 
    while degree > 0:
        minute += 60
        
    while second > 60:
        minute += 1
        second -= 60
        
    conversion += minute
    return conversion    

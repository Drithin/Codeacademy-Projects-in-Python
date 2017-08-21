def is_int(x):
  
  if type(x) == int or (type(x) == float and x%1.0==0):
    return True
  else:
    return False
 
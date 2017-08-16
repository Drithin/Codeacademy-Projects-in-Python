def is_int(x):
  if abs(x) != x:
     if type(x) == int or type(x) == float:
      return True
      print "It is True"
     else:
      return False
      print "It is False"
 
is_int(-3.4)
	def digit_sum(n):
	 s = 0
	 while n>0:
	    m = n%10
	    
	    n = n // 10
	    
	    s += m
	 return s


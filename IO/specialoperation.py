a = 10
b = 20
list = [10, 20, 30, 40, 50]

if(a in list):
   print "a is present in the given list"
else:
   print "a is not present in the given list"

if (b not in list):
   print "b is not present in the given list"
else:
   print "b is present in the given list"

a = 20
b = 20

if (a is b):
   print "a and b have same identity"
else:
   print "a and b do not have same identity"

if (id(a) == id(b)):
   print "a and b have same identity"
else:
   print "a and b do not have same identity"

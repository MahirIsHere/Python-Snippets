#Radix Sort Program

def radixsort(aList):
  RADIX = 10
  maxLength = False
  tmp, placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range(RADIX)]

    # split aList between lists
    for i in aList:
      tmp = int(i / placement)
      buckets[tmp % RADIX].append(i)
      if maxLength and tmp > 0:
        maxLength = False

    # empty lists into aList array
    a = 0
    for b in range(RADIX):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    # move to next digit
    placement *= RADIX


#User input
sort_list = list()
count = raw_input("Enter number of elements : ")

print
print 'Enter '+str(count) + ' numbers : '

print
for i in range(int(count)):
    n = raw_input("number"+str(i+1)+": ")
    sort_list.append(int(n))

radixsort(sort_list)

print
print "Elements in sorted order :"
print(sort_list)

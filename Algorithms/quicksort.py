def quickSort(alist):
   quickSortHelper(alist, 0, len(alist)-1)

#recursive function


def quickSortHelper(alist, first, last):
   if first < last:

       #partition the list
       splitpoint = partition(alist, first, last)

       # sort both halves
       quickSortHelper(alist, first, splitpoint-1)
       quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark - 1

       if rightmark < leftmark:
           done = True
       else:
           # swap places
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   # swap start with alist[first]
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark


num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) + ' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))

quickSort(num_array)
print "Sorted list in ascending order : "+str(num_array)

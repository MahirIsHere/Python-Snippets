#Shell Sort

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist, startposition, sublistcount)

      print "After increments of size", sublistcount, "The list is", alist

      sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = currentvalue


#User input
sort_list = list()
count = raw_input("Enter number of elements : ")

print
print 'Enter '+str(count) + ' numbers : '

print
for i in range(int(count)):
    n = raw_input("number"+str(i+1)+": ")
    sort_list.append(int(n))

print
shellSort(sort_list)

print
print "Elements in sorted order :"
print(sort_list)

from heapq import merge


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) + ' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))

print "Sorted list in ascending order : "+str(merge_sort(num_array))

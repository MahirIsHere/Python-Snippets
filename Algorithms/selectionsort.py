def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst


num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) + ' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))

print "Sorted list in ascending order : "+str(selection_sort(num_array))

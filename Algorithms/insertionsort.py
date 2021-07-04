def InsertionSort(list):
    for index in range(1, len(list)):
        curr = list[index]
        position = index

        while position > 0 and list[position-1] > curr:
            list[position] = list[position-1]
            position = position - 1

        list[position] = curr
    return list


num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) + ' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))

print "Sorted list in ascending order : "+str(InsertionSort(num_array))

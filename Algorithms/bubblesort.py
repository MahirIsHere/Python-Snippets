def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


alist = list()
num = input("\nEnter number of elements: ")

for i in range(int(num)):
	n = input("num: ")
	alist.append(int(n))

print("\nThe unsorted array: ")
print(alist)

bubbleSort(alist)

print("\nThe Sorted array: ")
print(alist)

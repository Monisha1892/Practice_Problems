# num_list = [20,48,16,2,56,90,34,1,7]
# count = 0
# for i in range(0,len(num_list)):
#     if num_list[i]>count:
#         count = num_list[i]
#     else:
#         count = count
# print(count)

# num_list = [48,20,16,2,56,90,34,1,7]
# count = 0
# for i in range(0,len(num_list)):
#     for j in range(i+1, len(num_list)):
#         if num_list[i] > num_list[j]:
#             count = num_list[i]
#             num_list[i] = num_list[j]
#             num_list[j] = count
#             print(num_list)
#         else:
#             pass
# print(num_list)





# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    temp = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                print(arr)



arr = [64, 34, 25, 12, 22, 11, 90]


bubbleSort(arr)

print ("Sorted array is:",arr)
# for i in range(len(arr)):
# 	print ("% d" % arr[i]),

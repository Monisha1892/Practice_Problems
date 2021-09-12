# Program to multiply two matrices using nested loops

# take a 3x3 matrix
A = [[12, 7, 3, 1],
     [4, 5, 6, 1],
     [7, 8, 9, 1]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

if len(A[0]) == len(B):
    print("yes")
else:
    print("no")
    if len(A[0]) > len(B):
        n = len(A[0]) - len(B)
        print("1: ",n)
        for i in range(n):
            B.append([0]*len(B[0]))
    else:
        n = len(B) - len(A[0])
        print("2: ",n)
        print(len(A[0])+n)
        # for i in range(0,len(A)):
        #     for j in range(len(A[0]), len(A[0])+n):
        for i in A:
            for j in range(n):
                i.append(0)

print(A)
print(B)



result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterating by row of A
for i in range(len(A)):

    # iterating by column by B
    for j in range(len(B[0])):

        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)

[114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]

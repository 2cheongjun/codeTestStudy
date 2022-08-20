N = int(input()) #1
result = 0 #2
for i in range(1, N+1) :  
    A = list(map(int, str(i))) #3
    result = i + sum(A) #4
    if result == N : #5
        print(i)
        break

    if i==N: #6
        print(0)
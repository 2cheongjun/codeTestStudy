N = int(input())

count = 0 
for i in range(3, N+1):
    count+= str(i).count('3')
    count+= str(i).count('6')
    count+= str(i).count('9')
print(count)
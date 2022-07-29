*min, max로 풀기 
N = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))


*sort로 풀기 
N=int(input())
array=list(map(int,input().split()))
array.sort()
print(array[0],array[-1])#array[0], array[-1] index 처음과 마지막을 출력한다.


*list index로 풀기
n = int(input())
numbers = list(map(int, input().split()))
max  = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)

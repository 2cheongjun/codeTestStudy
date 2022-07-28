N = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))


*sort로 풀기 
N=int(input())
array=list(map(int,input().split()))
array.sort()
print(array[0],array[-1])#array[0], array[-1] index 처음과 마지막을 출력한다.

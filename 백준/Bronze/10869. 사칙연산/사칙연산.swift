import Foundation

let input = readLine()!
let arr = input.split(separator:" ")
let A = Int(arr[0])!
let B = Int(arr[1])!
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)


# 파이썬
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b) /로 하면 2.3333333333333335 나옴 //해야 결과의 몫을 가져옴
print(a%b)

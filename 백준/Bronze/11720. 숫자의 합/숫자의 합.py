n = int(input())

nums = input()

total = 0
for i in range(n):
    total += int(nums[i])
print(total)


*sum으로 풀기
// 문자열을 정수로 전환
n = int(input())
// 합(정수로전환한 숫자들의합)
print(sum(map(int, input())

import sys
from collections import defaultdict
input = sys.stdin.readline

books = defaultdict(int)
n = int(input())

for _ in range(n):
    book = input().rstrip()
    books[book] += 1

books = sorted(books.items())
print(sorted(books, key = lambda x : -x[1])[0][0])
import numpy as np

str = input().lower()

visited = []

for i in range(26):
    visited.append([0, 1])

max = 0
length = 0
for i in range(len(str)):
    c = str[i]
    visited[ord(c) - 97][0] += 1
    if visited[ord(c) - 97][0] <= visited[ord(c) - 97][1]:
        length += 1
    if visited[ord(c) - 97][0] > visited[ord(c) - 97][1]:
        visited[ord(c) - 97][1] += 1
        length = 1
    if length > max:
        max = length

print(str, max)

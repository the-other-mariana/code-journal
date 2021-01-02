import numpy as np

str = input().lower()

visited = []

for i in range(26):
    # counter, times checked
    visited.append([0, 1])
start = 0
end = 0
max = 0
length = 0
for i in range(len(str)):
    c = str[i]
    visited[ord(c) - 97][0] += 1
    if visited[ord(c) - 97][0] <= visited[ord(c) - 97][1]:
        end += 1
        length += 1
    if visited[ord(c) - 97][0] > visited[ord(c) - 97][1]:
        visited[ord(c) - 97][1] += 1
        length = 1
        for j in range(start, end):
            visited[ord(str[j]) - 97][1] = visited[ord(c) - 97][1]
        start = i
        end = start
    if length > max:
        max = length
    #print(c, length, max, visited)

print(str, max)

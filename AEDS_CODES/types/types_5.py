word1 = int(input())
values = input().split(" ")
values = list(map(int, values))
#print(values)
result = 1
for i in range(len(values) - 3, len(values), 1):
    result = result * values[i]
print(result)
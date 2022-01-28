n = int(input())
i = 1
result = 0
while i < n:
    i = i * 2
    if i == n:
        result = 1
    else:
        result = 0
if result == 1:
    print("YES")
else:
    print("NO")

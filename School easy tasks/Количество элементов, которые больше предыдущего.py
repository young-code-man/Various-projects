p = int(input())
a = 0
while p != 0:
    next = int(input())
    if next != 0 and p < next:
        a += 1
    p = next
print(a)

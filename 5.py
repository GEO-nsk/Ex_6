N = int(input())
a = set()
b = set()
for itr in range(1,N+1):
    a.add(itr)

for itr in range(2,N+1):
    for item in a:
        if item % itr == 0 and item != itr:
            b.add(item)

print(a-b)
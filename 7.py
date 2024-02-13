ptr = str(input())
a = set()
for itr in ptr.split():
    a.add(itr)

a = sorted(a)

print(a)
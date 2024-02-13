ptr = str(input())
num = str(input())

a = set()
b = set()

for itr in ptr.split():
    if itr in a:
        b.add(itr)
    a.add(itr)

if num in b:
    print('принадлежит')
else:
    print('не принадлежит')


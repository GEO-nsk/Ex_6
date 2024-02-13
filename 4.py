ptr1 = str(input())
ptr2 = str(input())
num = str(input())

a = set()
b = set()
c = set()

for itr in ptr1.split():
    a.add(itr)
for itr in ptr2.split():
    b.add(itr)

c = a & b
if num in c:
    print('приналдежит')
else:
    print('не принадлежит')


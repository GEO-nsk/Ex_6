a = set()
b = set()

ptr1 = str(input())
N = int(input())
for itr in ptr1.split():
    a.add(itr)

for itr in range(N):
    likes = str(input())
    for i in likes.split():
        b.add(i)

print(a-b)
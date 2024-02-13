a = set()

N = int(input())
for itr in range(N):
    course = str(input())
    for item in course.split():
        a.add(item)

print(len(a))

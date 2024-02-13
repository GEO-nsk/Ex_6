ptr = str(input())
a = set()
for itr in ptr.split():
    a.add(itr)
numbers = list(a)
final_list = []

for itr in numbers:
    new_a = set()
    new_a.add(itr)
    final_list.append(new_a)
    for item in range(len(final_list)-1):
        new_a = set()
        new_a |= (final_list[item])
        new_b = set()
        new_b.add(itr)
        new_a = new_a | new_b
        final_list.append(new_a)

final_list.pop(-1)

K = int(input())
list = []

for itr in final_list:
    if len(itr) == K:
        list.append(itr)

print(list)
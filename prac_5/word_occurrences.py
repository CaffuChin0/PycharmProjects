ss = input("Text: ")
ll = list(ss)

new_ll = []

for i in ss:
    if i not in new_ll:
        new_ll.append(i)

d = {}

for i in new_ll:
    d[i] = ll.count(i)

print(d)

from random import shuffle

abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
abc_list = []

for c in abc:
    abc_list.append(c)

shuffle(abc_list)

print("KEY:","".join(abc_list))
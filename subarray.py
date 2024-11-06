array = [-2,7,-3,4]
sub = []
for i in range(len(array)):
    sub_i = []
    for j in range(len(array)):
        if i != j:
            sub_i.append(array[j])
    sub.append(sub_i)
print(sum([i for i in max(sub)]))

    






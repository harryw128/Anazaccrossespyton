with open('crosses.txt') as f:
    lines = f.readlines()
print(lines)

new_list = [s.replace("\n", "") for s in lines]

print(new_list)

sorted_list = sorted(new_list)

print(sorted_list)

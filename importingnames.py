#opens crosses fill and read lines
with open('crosses.txt') as f:
    lines = f.readlines()
print(lines)
#prints out names from txt file

#removes /n after all names
new_list = [s.replace("\n", "") for s in lines]

print(new_list)
#prints out new list

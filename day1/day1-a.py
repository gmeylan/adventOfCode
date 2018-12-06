sum = 0
with open('input') as file:
    for line in file:
        if(line[:1]) == '+':
            sum = sum + int(line[1:])
        if(line[:1]) == '-':
            sum = sum - int(line[1:])

print(sum)
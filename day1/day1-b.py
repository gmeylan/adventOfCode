sum = 0
frequencies = []
frequencies.append(0)
not_reached = True

while True and not_reached:
    with open('input') as file:
        for line in file:
            if not_reached:
                if(line[:1]) == '+':
                    sum = sum + int(line[1:])
                if(line[:1]) == '-':
                    sum = sum - int(line[1:])
                if sum in frequencies:
                    print(sum)
                    not_reached = False
                    print(len(frequencies))
                frequencies.append(sum)
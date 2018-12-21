exactly_two = 0
exactly_three = 0
with open('input') as file:
    for line in file:
        seen_two_times = False
        seen_three_times = False
        character_set = ''.join(set(line.rstrip()))
        print('character_set', repr(character_set))
        for character in character_set:

            print('character', character)
            number = line.count(character)
            if number == 2 and not seen_two_times:
                seen_two_times = True
                print('found 2 times in:', character, line)
                exactly_two += 1
            if number ==  3 and not seen_three_times:
                seen_three_times = True
                print('found 3 times in:', character, line)
                exactly_three += 1
print(exactly_three, exactly_two)  
sum = exactly_three * exactly_two
print(sum)
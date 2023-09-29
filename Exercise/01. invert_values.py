# First way

list_with_numbers = input().split()
opposite_numbers = []
for number in list_with_numbers:
    current_number = -int(number)         #second option f"-{number}"
    opposite_numbers.append(current_number)

print(opposite_numbers) 

# Second way   

([-input(number) for number in input().split()])
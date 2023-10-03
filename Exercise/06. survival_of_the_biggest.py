numbers = input()
magic_number = int(input())
current_number = []
for number in numbers:
    current_input = number
    if current_input < number:
        current_number.append(number)
    
            
    
print(current_number)    
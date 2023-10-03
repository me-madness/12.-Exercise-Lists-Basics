numbers = input()
magic_number = int(input())
current_number = 0
for number in numbers:
    if current_number < number:
        current_number = int(number)
        print(current_number, end=" ")
    
            
    
# print(current_number)    
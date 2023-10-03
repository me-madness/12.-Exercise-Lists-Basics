numbers = input().split()
magic_number = int(input())
current_number = []
for number in numbers:
    current_number.append(number)
for _ in range(magic_number):
    current_number.remove(min(current_number))    
            
    
print(*current_number, sep=", ")    
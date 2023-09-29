# First option

multiply_number = int(input())
range_number = int(input())

list_digit = []

for num in range(1,range_number + 1):
    current_number = num * multiply_number
    list_digit.append(current_number)
    
print(list_digit)    

# Second option

multiply_number = int(input())
range_number = int(input())

list_digit = []

for num in range(1,range_number + 1):
    current_number = list_digit.append(num * multiply_number)
    
print(list_digit)
line_of_input = input().split(", ")
count_of_beggars = int(input())
money_integers = []
for current_money in line_of_input:
    money_integers.append(int(current_money))
final_sum = []
start_index = 0
while start_index < count_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_integers),count_of_beggars):
        current_beggar_sum += money_integers[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
    
print(final_sum)    
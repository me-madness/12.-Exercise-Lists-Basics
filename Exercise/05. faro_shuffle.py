deck_of_card = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_of_card) // 2
    left_part = deck_of_card[0:middle_of_deck]
    right_part = deck_of_card[middle_of_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_card = deck_after_shuffling    
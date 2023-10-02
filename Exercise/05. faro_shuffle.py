deck_of_card = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_of_card) // 2
    left_part = deck_of_card[0:middle_of_deck]
    right_part = deck_of_card[middle_of_deck:]
    deck_after_shuffling = []
    for card
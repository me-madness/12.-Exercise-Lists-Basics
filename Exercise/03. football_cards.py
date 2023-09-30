team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
card_input = input()
red_card = False

empty_list = [] 

for card in range(card_input):
    if "A-" in card:
        card.remove(team_a)
    elif "B-" in card:
        card.remove(team_b)   
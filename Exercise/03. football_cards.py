team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
card_input = input().split(' ')
red_card = False

# empty_list = [] 

for card in card_input:
    if "A-" in card:
        team_a.remove(card)
    elif "B-" in card:
        team_b.remove(card)   
        print(f"Team A - {team_a}; Team B - {team_b}.")
        if team_a < 7 or team_b < 7:
            red_card = True   
            print("Game was terminated")        


import random
import os

os.system("cls")
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generate_random_card():
    return card[random.randint(0, len(card) - 1)]

def is_player_bust(player_score):
    if player_score > 21:
        return True
    else:
        return False

def check_scores(player_score, computer_score, player_final_hand, computer_final_hand):
    if player_score == computer_score:
        return f"Your final hand: {player_final_hand} Player score: {player_score}\nComputer final hand: {computer_final_hand} Computer score: {computer_score}\nIt's a draw!"
    elif player_score > computer_score:
        return f"Your final hand: {player_final_hand} Player score: {player_score}\nComputer final hand: {computer_final_hand} Computer score: {computer_score}\nYou win!"
    else:
        return f"Your final hand: {player_final_hand} Player score: {player_score}\nComputer final hand: {computer_final_hand} Computer score: {computer_score}\nYou lose!"
        
    
play_blackjack = ''
while play_blackjack != 'y' and play_blackjack != 'n':
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if play_blackjack == 'n':
        break
    elif play_blackjack == 'y':
        players_cards = []
        computers_cards = []
        players_cards.append(generate_random_card())
        players_cards.append(generate_random_card())
        computers_cards.append(generate_random_card())
        game_in_progress = True
        while game_in_progress:
            print(f"Your cards: {players_cards}, current score: {sum(players_cards)}")
            print(f"Computer's first card: {sum(computers_cards)}")
            draw_card = ''
            while draw_card != 'y' and draw_card != 'n':
                draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_card == 'y':
                    players_cards.append(generate_random_card())
                    if is_player_bust(sum(players_cards)) == True:
                        print(f"Your cards: {players_cards}, Final score: {sum(players_cards)}")
                        print(f"Computer's final hand: {sum(computers_cards)}")
                        print("You've bust. You lose!")
                        game_in_progress = False
                elif draw_card == 'n':
                    while sum(computers_cards) < 17:
                        computers_cards.append(generate_random_card())
                    if sum(computers_cards) > 21:
                        print(f"Your cards: {players_cards}, Your final score: {sum(players_cards)}")
                        print(f"Computer's final hand: {computers_cards}, Computers final score {sum(computers_cards)}")
                        print("You Win. Computer has bust!")
                    else:
                        winner = check_scores(sum(players_cards), sum(computers_cards), players_cards, computers_cards)
                        print(winner)
                    game_in_progress = False




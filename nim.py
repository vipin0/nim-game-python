import random

def create_piles():
    pile_a = random.randint(5,15)
    pile_b = random.randint(5,15)
    pile_c = random.randint(5,15)

    return {'A':pile_a,'B':pile_b,'C':pile_c}

def choose_pile(piles,player):
    while True:
        pile = input(f'Player {player}, choose your pile (A, B, C) : ').strip()
        if pile in piles.keys():
            if piles[pile] == 0:
                print('ERR: Sorry, this pile is already empty.')
            else:
                return pile
        else:
            print('ERR: Sorry, that is not a valid pile.')

def print_piles(piles:dict):
    sizes = []
    for k,v in piles.items():
        sizes.append(v)
        print(f'{k}: {"*"*v}')
    print(tuple(sizes))

def check_all_piles_empty(piles:dict):

    for v in piles.values():
        if v>0:
            return False
    return True

def print_winner(player):
    print(f'\n\nPlayer {player} picked up the last object. <<< Player {player} >>> is the WINNER.')
    print('Thanks for playing. Goodbye.')

def get_pile_input(piles,pile):
    while True:
        num = input('Choose how many objects to remove : ').strip()
        if not num.isdigit():
            print('ERR: Sorry, that is not a valid number.') 
        else:
            num = int(num)
            if num > piles[pile]:
                print('ERR: Sorry, there is not enough objects to remove in this pile.')
            else:
                return num

def play_game(piles):
    print("===== Welcome to Nim Game =====")
    print("Here are the three piles")
    print_piles(piles)

    while True:
        pile = choose_pile(piles,1)
        pile_to_remove = get_pile_input(piles=piles,pile=pile)
        print('OK')
        piles[pile]-=pile_to_remove
        print_piles(piles)
        if check_all_piles_empty(piles=piles):
            print_winner(1)
            break
        
        pile = choose_pile(piles,2)
        pile_to_remove = get_pile_input(piles=piles,pile=pile)
        print('OK')
        piles[pile]-=pile_to_remove
        print_piles(piles)
        if check_all_piles_empty(piles=piles):
            print_winner(2)
            break
    
if __name__ == '__main__':
    piles = create_piles()
    play_game(piles)


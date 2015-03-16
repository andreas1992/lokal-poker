spillere = []
pot = 0

def dealer(player, money):
    spillere.append([player, money])

def make_bet(bet, spillernr):
    index = spillernr
    print spillere[index]
    global pot
    pot = pot + bet
    a = spillere[index]
    print a[1]
    a[1] = a[1] - bet

def poker_round():
    index = 0
    while index < len(spillere):
        betting = raw_input("hva er ditt bet?")
        playerBet = int(betting)
        make_bet(playerBet, index)
        player = index
        listPlayer = spillere[index]
        index += 1
        if index == len(spillere):
            index = 0
        elif playerBet == 0:
            del spillere[player]
            index -= 1
        
# def print_player(index):
    
# def print_pot():
    
# def print_all_players():
    
# def add_player():

# def give_pot():



    
    


# dealer("Andreas", 1000)
# dealer("Linda", 1000)
# dealer("Frank", 1000)

# poker_round()

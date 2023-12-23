import random


def main():
    """ 
        Main game screen
    """
    num_par = num_participants(1,5,"players")
    player_names = names(num_par)
    new_game = scoreboard(player_names)
    


    return 

def names(num_par:int)-> dict:
    """
        Add the names of the players
    """
    player_names = {}
    for i in range(1, num_par + 1, 1):
        while True:
            name = str(input(f"Name of player {i}: "))
            if name in player_names:
                print("That name was already picked!")
                continue
            else:
                player_names[name]= 0
                break
            
    return player_names


# def scoreboard(player_names:dict) -> list:



#     return list
    


def roll():
    """ Roll dice """
    min_v = 1
    max_v = 6

    roll = random.randint(min_v, max_v)
    
    return roll

      

def num_participants(min_par:int,  max_par:int, par_info:str="participants") -> int: #par_info can be any kind of name describing the participants, for example, players, users, patients, etc.
    """
        This function allows to select the amount of participants 
        with a min and max specified in the function.
        Precondition: min_par an int, max_part an int and par_info a string.
        Postcondition: participants an int. It is the resulting amount of participants.
    """

    while True:
        try: 
            participants = int(input(f"Enter the number of {par_info} ({min_par}-{max_par}): "))
            if not min_par <= participants <= max_par: 
                print(f"Number of {par_info} invalid")
                continue
        except ValueError:
            print("It needs to be a whole number!")
            continue

        else:
            return participants







from ocean import *
from player import *
from ship import *
from square import *
from main import main
import os


class GameFlow():

    turn_count = 0
    difficulty_lvl = 0
    play_mode = ''

    def __init__(self):

        self.player_one = self.choose_play_mode()
        self.player_two = Human(self.choose_players_name())

    def fight(self):

        while True:
            self.turn_count += 1
            self.player_one.perform_hit(self.player_two)
            if self.check_if_lose(self.player_two):
                print(self.player_two.board)
                print(self.player_one)
                return self.player_one
            self.player_two.perform_hit(self.player_one)
            if self.check_if_lose(self.player_one):
                print(self.player_one.board)
                print(self.player_two)
                return self.player_two

    def check_if_lose(self, player):

        total_hit_points = 0
        for ship in player.board.my_navy:
            total_hit_points += ship.hit_points
        if total_hit_points == 0:
            return True
        return False

    def choose_play_mode(self):
        play_modes = ['Choose game mode:', ' 1. Singleplayer', ' 2. Multiplayer']
        while True:
            self.print_list(play_modes)
            mode = input(" Pass mode number: ")
            if mode == '1':
                self.play_mode = 1
                return AI()
            elif mode == '2':
                self.play_mode = 2
                return Human(self.choose_players_name())
            else:
                print('Input must be a number from given scope.\n')

    def choose_players_name(self):
        os.system('clear')
        name = ''
        while len(name) == 0:
            name = input("Choose players name: ").strip()
        os.system('clear')

        return name

    @staticmethod
    def print_list(list):
        for element in list:
            print(element)

    def set_difficulty_lvl(self):   # podpiąć jak już sie zdecydujemy, czym się różnią poziomy
        levels = ['\n1. Easy', '2. Medium', '3. Hard']
        self.print_list(levels)

        while True:
            difficulty_lvl = input("\nChoose number of difficulty level: ").strip()
            if difficulty_lvl in ["1", "2", "3"]:
                break
            else:
                print("Input must be a number from given scope.\n")

        self.difficulty_lvl = difficulty_lvl

    def init_hall_of_fame(self, filename):
        ''' Writes to hall_of_fame file.'''
        with open("HALL_OF_FAME.txt", "a", encoding='utf-8') as HALL_OF_FAME:
            user_score = [player.name, square.hit_count]                        #do ustalenia
            user_score = "        ".join(user_score)
            HALL_OF_FAME.write(str(user_score) + "\n")
            print("Wciśnij cokolwiek.")
            input_char = getch()

    def show_hall_of_fame(self, filename):
        ''' Reads from and prints hall_of_fame file.'''
        with open("HALL_OF_FAME.txt", "r", encoding='utf-8') as HALL_OF_FAME:
            os.system("clear")
            print("\nHALL_OF_FAME:\n")
            HALL_OF_FAME = sorted(HALL_OF_FAME.readlines(), reverse=True)
            list_place = 1
        for i in HALL_OF_FAME:
            print('{:04d}'.format(list_place), ".", "".join(i))
            list_place += 1
            print("Wciśnij 'Y' żeby zagrać jeszcze raz, coś innego żeby wyjść.")
            input_char = getch()
            os.system("clear")
            if input_char.upper() == "Y":
                main()
            sys.exit()


# test_gameflow = GameFlow()
# print('AAAAAAA')

# total_hp_ships = 0
# for ship in test_gameflow.player_two.board.my_navy:
#     print(ship)
#     total_hp_ships += ship.hit_points

# print(test_gameflow.player_two.board)   # wypisuje planszę playera z ustawionymi statkami
# # test_gameflow.choose_play_mode()    # niepotrzebne, bo powołując instancje wykonuje się init w którym to już jest
# print('hit_points:', total_hp_ships)
# test_gameflow.player_two.board.my_navy[0].decrement_hp()
# test_gameflow.player_two.board.my_navy[0].decrement_hp()

# test_gameflow.check_if_lose(test_gameflow.player_two)


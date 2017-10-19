from ship import *
from square import *
import sys


class Ocean():

    def __init__(self, ship_coordinates_dict, ocean_fields):
        self.ship_coordinates_dict = ship_coordinates_dict
        self.ocean_fields = ocean_fields
        self.my_navy = []   # list of refs to players ship objects
        self.__set_ships_on_board()

    def __set_ships_on_board(self):

        for ship in self.ship_coordinates_dict.keys():     # dla klucza = nazwie klasy w str
            ship_object = getattr(sys.modules[__name__], ship)()
            self.my_navy.append(ship_object)
            for list_of_coordinants in self.ship_coordinates_dict.get(ship):   # lista w lista list ze współrzędnymi
                for coordinants in range(len(self.ship_coordinates_dict.get(ship))):
                    x_coord = list_of_coordinants[0]    # współrzędna x
                    y_coord = list_of_coordinants[1]
                    self.ocean_fields[x_coord].pop(y_coord)    # wyczyść pozycję z pustego Square()
                    self.ocean_fields[x_coord].insert(y_coord, Square(ship_object))    # wstaw instancję Square zaimplementowaną konkretnym shipem


    def __str__(self):

        alfabet = "ABCDEFGHIJ"
        # title_bar = ' |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10 '

        title_bar = ' '
        for element in range(len(self.ocean_fields[0])):  # magic
            if element + 1 < 10:  # magic
                title_bar += '|  {}  '.format(element+1)  # magic
            else:
                title_bar += '|  {} '.format(element+1)    # magic

        separator = '-'*len(title_bar) + '\n'

        super_str = ''
        super_str += title_bar + '\n' + separator

        for lists in range(len(self.ocean_fields)):
            super_str += alfabet[lists]
            for element in range(len(self.ocean_fields[lists])):
                super_str += "|  {}  ".format(self.ocean_fields[lists][element].__str__())
            super_str += '\n'
            super_str += separator

        return(super_str)

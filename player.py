from main import *
from ocean import Ocean
from ship import Destroyer, Submarine, Cruiser, Battleship, Carrier
from square import Square
from game_flow import GameFlow


class Player(GameFlow):
    """Abstract Player class."""
    name = "Noname"
    # Player's availible ships:
    ships = [Destroyer, Submarine, Cruiser, Battleship, Carrier]
    my_ships = {}  # containts Player's created ships
    board = None  # Ocean object

    def perform_hit(self, opponent, coordinates):
        pass  # czekam na Anię :)

class Human(Player):
    """This is User-Player class."""

    def __init__(self, name):
        self.name = name
        # self.board = Ocean()
        self.choose_ships_placement()

    def choose_ships_placement(self):
        """Player choose ships placement (coordinates)."""
        self._input_coordinates()

    def _input_coordinates(self):
        """
        Input coordinates by User (format: A1, B1, etc..).

        Check if input is correct.
        Transform Player's coordinates to right indexing form.
        Get inputed x, y coordinates (format: [A, 1], [A, 2]).
        Tranform to format [0, 0] to use for correct indexing.
        """
        all_ships_coordinates = {}
        type_letter = "Please, specify X (choose letter between A - J): "
        correct_letters = "ABCDEFGHIJ"
        type_number = "Please, specify Y (choose number between 1 - 10): "
        invalid_input_info = "invalid input."
        for ship in self.ships:
            Human.choose_ship_picture(ship)
            ship_coordinates = []
            for element in range(ship.hit_points):
                coordinate = []
                while True:
                    try:
                        row_index = input(type_letter).upper()
                        if row_index in correct_letters:
                            coordinate.append(correct_letters.index(row_index))
                            break
                        else:
                            print(invalid_input_info)
                    except:
                        print(invalid_input_info)
                while True:
                    try:
                        column_index = int(input(type_number))
                        if column_index in range(1, 11):
                            coordinate.append(column_index - 1)
                            break
                        else:
                            print(invalid_input_info)

                    except:
                        print(invalid_input_info)
                ship_coordinates.append(coordinate)
                print(ship_coordinates)

            # metoda Michała - walidacja
            all_ships_coordinates[ship.__name__] = ship_coordinates
            print(all_ships_coordinates)  # temporary

    @staticmethod
    def choose_ship_picture(ship_instance):
        filenames = ["cruiser_PHOTO.md", "battleship_PHOTO.md",
                     "carrier_PHOTO.md", "submarine_PHOTO.md", "destroyer_PHOTO.md"]
        if ship_instance.__name__ == "Cruiser":
            Human.print_ship_picture("cruiser_PHOTO.md")
        elif ship_instance.__name__ == "Battleship":
            Human.print_ship_picture("battleship_PHOTO.md")
        elif ship_instance.__name__ == "Carrier":
            Human.print_ship_picture("carrier_PHOTO.md")
        elif ship_instance.__name__ == "Submarine":
            Human.print_ship_picture("submarine_PHOTO.md")
        elif ship_instance.__name__ == "Destroyer":
            Human.print_ship_picture("destroyer_PHOTO.md")

    @staticmethod
    def print_ship_picture(filename):
        with open(filename, "r", encoding="utf8") as myfile:
            myfile = myfile.read().splitlines()
            for line in myfile:
                print(line)


class AI(Player):
    """This is AI-Player class."""

    name = "AI"
    def __init__(self):
        self.board = Ocean()
        # self.get_my_ships()

    def generate_ships_placement(self):
        """AI generate ships placement (coordinates)."""
        pass

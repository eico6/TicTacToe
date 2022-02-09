import os

class Board:

    def __init__(self):
        self.slots = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9'
        ]

    def draw_board(self) -> None:
        os.system("cls")  # Will print out a rectangle if not ran from Windows Command Prompt
        print("")
        print(" ================")
        print(" = Tic-Tac-Toe! =")
        print(" ================")
        print("     -------")
        print("     |%s|%s|%s|" % (self.slots[0], self.slots[1], self.slots[2]))
        print("     |%s|%s|%s|" % (self.slots[3], self.slots[4], self.slots[5]))
        print("     |%s|%s|%s|" % (self.slots[6], self.slots[7], self.slots[8]))
        print("     -------")

    def insert_to_board(self, index: int, char: str) -> None:
        # PLAYER   = 'X'
        # COMPUTER = 'O'
        self.slots[index - 1] = char

    def is_slot_occupied(self, index: int) -> bool:
        # Return true if slot is occupied
        return True if self.slots[index - 1] != str(index) else False
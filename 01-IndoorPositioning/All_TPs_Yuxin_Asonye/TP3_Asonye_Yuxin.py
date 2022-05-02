# Hidden Markov Model

import sys


class Node():
    """
    Class that represent a Node in the Markov Model
    """

    def __init__(self):
        self.__move = 0
        self.__stat = 0.0

    def add_move(self):
        """
        Method that add a move to the cell's moves
        """
        self.__move += 1

    def get_move(self):
        """
        Method returning cell' moves
        """
        return self.__move

    def get_stat(self):
        """
        Method that return the cell proba
        """
        return self.__stat

    def set_stat(self, stat):
        self.__stat = stat

    def __str__(self):
        """
        Method to print a cell
        """
        return "[ " + str(self.__move) + "," + str(self.__probability) + " ]"


class Chain():
    """
    Class that represent a Markov Chain
    """

    def __init__(self, nb_cells):
        self.__nb_cells = nb_cells
        self.__curent = 0
        self.__previous = 0
        self.__nodes = []
        # Creating a n*n matrix where n=nb_cells
        for i in range(nb_cells):
            self.__nodes.append([])
            for j in range(nb_cells):
                self.__nodes[i].append(Node())

    def move_to(self, cell_id):
        """
        Method to move from a cell to another
        """
        self.__nodes[self.__curent][cell_id].add_move()  # Counting the moves
        self.refresh(self.__previous)  # Re computing probability
        self.__previous = self.__curent
        self.__curent = cell_id

    def refresh(self, previous):
        """
        Method that re compute cell probability
        """
        for i in range(self.__nb_cells):
            self.__nodes[previous][i].set_stat(
                self.__nodes[previous][i].get_move()/self.get_line_count(previous))

    def get_next_move(self):
        """
        Method to get the most likely next move
        """
        max_move = 0
        id = 0
        for i in range(self.__nb_cells):
            if self.__nodes[i][self.__curent].get_move() > max_move:
                max_value = self.__nodes[i][self.__curent].get_move()
                id = i

        return id

    def get_line_count(self, line_index):
        """
        Method to get the total moves for the specified line
        """
        total = 0
        for i in range(self.__nb_cells):
            total += self.__nodes[line_index][i].get_move()

        return total

    def get_column_count(self, column_index):
        """
        Method to get the total moves for the specified column
        """
        for i in range(self.__nb_cells):
            total += self.__nodes[i][column_index].get_move()

        return total

    def print_tab(self):
        for i in range(19):
            print(" ", end='')

    def print_line_separator(self):
        print("+------------------", end='')
        for i in range(self.__nb_cells):
            print("+---------------------------", end='')
        print("+", end='')
        print("--------------+")

    def print(self):
        """
        Method to print the tab of moves and probability of the whole chain
        """
        separator = "+---------------------------"

        print("\n")
        # Printing titles
        self.print_tab()
        print("| ", end='')
        for i in range(self.__nb_cells):
            title = "Current page: " + str(i)
            print(title, end='')
            for j in range((len(separator) - len(title)) - 2):
                print(" ", end='')
            print('| ', end='')
        print("Total Lines |")

        # Printing lines and columns
        for i in range(self.__nb_cells):
            self.print_line_separator()
            previous = "Previous Page: " + str(i) + " "
            for j in range(self.__nb_cells):
                if j == 0:
                    print(previous, end='')

                contain = "| Moves: " + str(self.__nodes[i][j].get_move()) + ", Stat: " + str(
                    "%.2f" % (self.__nodes[i][j].get_stat()*100)) + "% "
                print(contain, end='')

                for k in range(len(separator) - len(contain)):
                    print(" ", end='')
            print("| ")

        print("\n")

    def get_current(self):
        """
        Method to get current cell
        """
        return self.__curent

    def get_previous(self):
        """
        Method to get previous cell
        """
        return self.__previous

    def get_cell_number(self):
        """
        Method to get cell number
        """
        return self.__nb_cells


if __name__ == "__main__":
    # The Markov Chain
    chain = Chain(5)

    while(True):
        print("You are coming from the page " + str(chain.get_previous()) +
              "." + "\nYou are on the page " + str(chain.get_current()))
        go_to = input("choose a page to go (between 0 and " +
                      str(chain.get_cell_number()) + ") or q to quit: ")

        # If the user inout isn't correct
        if isinstance(go_to, int):
            while((int(go_to) < 0) and (int(go_to) > chain.get_cell_number())):
                go_to = input("choose a page to go (between 0 and " +
                              str(chain.get_cell_number()) + ") or q to quit: ")

        # If the user input is q, we quit the programm
        if go_to == 'q':
            print("exit the program...")
            sys.exit(0)

        # Moving to the cell given in input
        chain.move_to(int(go_to))

        # Printing the actual chain
        chain.print()

        # Printing the predicted next move
        print("You can certainly goto " + str(chain.get_next_move()))

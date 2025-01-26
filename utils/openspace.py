import random
import pandas as pd
from collections.abc import Sequence
from .table import Table
from prettytable import PrettyTable


class Openspace:
    """
    A class which mimics the office setup with tables.
    Each instance has a list of tables and the number of tables

    """

    def __init__(self, capacity: int, number_of_tables: int) -> None:
        """
        Constructor which initialises the object

        :param capacity: int with number of seats in each table
        :param number_of_tables :int with tables in the openspace
        :return Openspace object :obj with Tables in an office space
        """
        # Create the object with the required parameters
        self.capacity = capacity
        self.number_of_tables = number_of_tables
        self.tables = [Table(capacity) for _ in range(number_of_tables)]

    def __str__(self) -> str:
        """
        Returning a string representation of the object instead of the memory adress of the object
        """
        return "An office space with {self.number_of_tables} tables and {self.capacity} seats per table".format(
            self=self
        )

    def display(self) -> None:
        """
        Function which will display the overlay of the office tables.
        No explicit parameters just the self object
        """
        # Creating a prettytable package object
        print("\n")
        workspace = []
        workspace_table = PrettyTable()

        # Create the header with Tables,Seat1, Seat2...Seatn
        headers = ["Seat " + str(i + 1) for i in range(self.capacity)]
        headers.insert(0, "Tables")

        # Loop through the Seat objects within Table object to get the occupant name
        for index, each_table in enumerate(self.tables):
            table = ["Table " + str(index + 1)]
            for each_seat in each_table.seats:
                table.append(each_seat.occupant)
            workspace.append(table)

        # Populate the prettytable wuth title, headers and rows and print it
        workspace_table.title = "Openspace Worktables"
        workspace_table.field_names = headers
        workspace_table.add_rows(workspace)
        print(workspace_table)

    def priority(self, wishlist: Sequence, names):
        """
        Function which prioritises peoples wishes of sitting together at the same table.

        :param wishlist: A list of people who needs to be placed at the same tables.
        :return number_of_spots: An int which says how many spots are left
        :return names: A list with the rest of the people to be placed
        """
        number_of_spots = self.number_of_tables * self.capacity
        for index,group in enumerate(wishlist):
            for each in group:
                if each != "None":
                    self.tables[index].assign_seat(each)
                    names.remove(each)
                    number_of_spots -=1 
        self.display()
        return (number_of_spots, names)

    def organize(self, names: Sequence, number_of_spots) -> int:
        """
        Function which will assign each person in the list given a random table.

        :param names: A list of people need to be placed at the tables.
        :return number_of_spots: An int which says how many spots are left
        :return names: A list with the people not placed yet at tables
        """
        # Loop till there are still occupants to place in tables and free spots
        # Number of spots across all tables is calculated on the fly
        #number_of_spots = self.number_of_tables * self.capacity
        while names and number_of_spots:
            rand_tab = random.randint(0, self.number_of_tables - 1)
            if self.tables[rand_tab].has_free_spot():
                self.tables[rand_tab].assign_seat(names[0])
                names.pop(0)
                number_of_spots -= 1
        return (number_of_spots, names)

    def store(self, filename: str) -> None:
        """
        Function which will store the table structure in the given excel file.

        :param filename: A string which has the name of the excel file to save the table layout
        """
        # Create a list of lists of occupants to save in an excel file
        workspace = [
            [each_seat.occupant for each_seat in each_table.seats]
            for each_table in self.tables
        ]
        to_save = pd.DataFrame(workspace)
        to_save.to_excel(filename, header=False, index=False)

    def new_members(self, names: Sequence) -> Sequence[str]:
        """
        Function which adds the given extra names to the Openspace

        :param names: A list with names of people to add
        :return list: A list of names that still are not placed in a table 
        """
        modify_names = list(names)
        for name in names:
            for each_table in range(len(self.tables)):
                if self.tables[each_table].has_free_spot():
                    self.tables[each_table].assign_seat(name)
                    modify_names.pop(0)
                    break
        return modify_names

    def reorganise(self, empty_spots: int, names: Sequence) -> None:
        """
        Function which modifies the existing table layout of the openspace

        :param empty_spots: An int which is the number of spots left after a round of placing people on tables 
        :params names: A list of names that still need to be placed on a table 
        """
        if empty_spots > 0:
            leftovers = self.new_members(names)
            if leftovers:
                self.add_table(leftovers)
        else:
            self.add_table(names)
        
    def add_table(self, names: Sequence) -> int:
        """
        Function which adds a table to the layout of the openspace

        :params names: A list of names to be placed on the table 
        :return int: The number of spots still left at the table
        """
        new_ppl = len(names)
        while new_ppl>0:
            self.tables.append(Table(self.capacity))
            for each in names:
                self.tables[-1].assign_seat(each)
            names = names[self.capacity:]
            new_ppl -= self.capacity
        return self.tables[-1].left_capacity()
    
    def check_loner(self) -> None:
        """
        Function to check if someone is alone at a table

        If the last table has only one member, it pulls a person from the table before and assigns them a new place
        """
        if self.capacity - self.tables[-1].left_capacity() == 1:
            print("\nLooks like we have a loner in the last table. Lets rearrange.\n")
            new_company = self.tables[-2].seats[-1].remove_occupant()
            self.tables[-1].assign_seat(new_company)
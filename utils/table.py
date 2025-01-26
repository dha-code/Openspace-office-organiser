# Creation of seat class that will be used to create the seats for each table
class Seat:
    def __init__(self, free: bool, occupant: str):
        self.free = free
        self.occupant = occupant

    # Checks if a seat is free
    def set_occupant(self) -> bool:
        """if the seat (self.free) is free, it returns True
        if not it returns False"""
        if self.free:
            return True
        else:
            return False

    # Removes someone from a seat
    def remove_occupant(self) -> str:
        """Change the seat to True with no occupant --> the seat can be used again by someone else
        and returns the name that was on this seat previously"""
        self.free = True
        name = self.occupant
        self.occupant = None
        return name

    def __str__(self):
        """Tells you if the seat is free. if it's not it gives you the name of the occupant and if it is, the occupant is None"""
        return f"This seat is free: {self.free} and the occupant is {self.occupant}"


# Creation of the table class --> creation of all the tables based on the number of seats possible per table
class Table:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats = [Seat(True, None) for _ in range(capacity)]
        # We make a loop to add seats in a list for each table created. The loop depends on the capacity (number of seats available)
        # If we want smaller or bigger table, the option is available. We're not limited to 4 seats per table

    # Checks if a table is full or not
    def has_free_spot(self) -> bool:
        """Using the function below that gives the number of free spots still available on the table
        if it is higher than zero then that means there are still seats avaiblable and it returns True.
         In the other case (if no seats are available), it returns False"""
        if self.left_capacity() > 0:
            return True
        else:
            return False

    # Places someone at the table
    def assign_seat(self, name: str) -> bool:
        """it's using the function above to chakc if there are still seats available
        if it's the case, it's checking each seat in the table until it finds a free seat.
         When it does, it changes the status "free" to False and the occupant from None to the name of the person
         If no seats are available, it returns False (just in case) --> if has_free_spot has been called before trying to add a name, it shouldn't be necessary
        """
        if self.has_free_spot():
            for seat in self.seats:
                if seat.set_occupant():
                    seat.free = False
                    seat.occupant = name
                    self.left_capacity()
                    return True
                else:
                    continue
        else:
            return False

    # Checks how many seats are available on a table
    def left_capacity(self) -> int:
        """We start at zero and we make a loop in the table to check for any seat available
        Each time a seat is available we add +1 to the count, which is the new capacity of the table
        It returns the number of seats still available"""
        count = 0
        for i in self.seats:
            if i.free:
                count += 1
            else:
                continue
        self.capacity = count
        return self.capacity

    def __str__(self):
        """Tell you the total number of seats and the number of seats still available in a specific table"""
        return f"This table contains {self.capacity} seats left and has {len(self.seats)} in total"

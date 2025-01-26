import yaml
import pandas as pd
from utils.openspace import Openspace
from utils.file_utils import read_file,wishlist

# Reading the config file to extract information
config = yaml.safe_load(open("./data/config.yml"))
names = read_file(config["file"])
number_of_tables = config["number_of_tables"]
capacity = config["capacity"]

# Create Openspace object from parameters in the config file
openspace = Openspace(capacity, number_of_tables)

# Let the code organise people randomly on the tables
print("\nWelcome to Openspace!")
print(f"\nYour office space has {number_of_tables} tables with {capacity} seats each.")
print(f"\nTrying to place {len(names)} people on the tables.")

# If there is a wishlist, prioritse that 
if "wishlist" in config:
    wishlist = wishlist(config["wishlist"])
    (number_of_spots, names) = openspace.priority(wishlist, names) 
    print(f"\nWishlist satisfied. We will now place the other {len(names)} people.")

(empty_spots, leftover_names) = openspace.organize(names, number_of_spots)
print(f"\nThere are {empty_spots} seat(s) left.")

# If there are people not placed in the tables, add new tables
if leftover_names:
    print("\nLooks like we have more people that seats available. Adding new tables.")
    empty_spots = openspace.add_table(leftover_names) 

# If the config has an extra file of newcomers, add them to Openspace
if "latecomers" in config:
    new_people = read_file(config["latecomers"])
    print("\nThere seems to be new people coming in. Adding them to the Openspace.")
    openspace.reorganise(empty_spots, new_people)

# Check if there is someone alone in a table and then finally display the openspace layout
openspace.check_loner()
openspace.display()

# Save the table layout in an output excel file
openspace.store("./data/table_layout.xlsx")
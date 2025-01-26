import pandas as pd


# make a list with all elements from the excel file
def read_file(filename: str) -> list:
    """
    Create a dataframe with the Excel file, indicating there's no header --> then we have the first name included in the list
    we go through all elements in the excel file and add it to the list --> the excel file can only contain names

    :params filename: str Name of the excel file
    :return list: A list of names
    """
    df = pd.read_excel(filename, header=None)
    # Iterate through the column of the dataframe and add each element in a list
    for element in df.columns:
        list_names = df[element].tolist()
    return list_names

def wishlist(filename: str) -> list:
    """
    Function which reads the wishlist where people want to sit to next to each other

    :params filename: str Name of the excel file
    :return list: A list of names who wants to sit together
    """
    df = pd.read_excel(filename, header=None)
    df = df.fillna('None')
    wish_list = df.values.tolist()
    return wish_list

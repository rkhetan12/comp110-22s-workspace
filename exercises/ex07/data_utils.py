"""Dictionary related utility functions."""

__author__ = "730476155"

# Define your functions below

from csv import DictReader


def read_csv_rows(file_and_path: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]`."""
    new_list: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(file_and_path, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather that just strings
    entire_file = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in entire_file:
        new_list.append(row)

    # Close tha file wjen we're done, to free its resources
    
    file_handle.close()
    return new_list


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a `list[str]` of all values in a single `column` whose name is the second parameter."""
    new_list: list[str] = []
    for row in table:
        item: str = row[column]
        new_list.append(item)
    return new_list


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a colum-oriented table."""
    new_dict: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        new_dict[column] = column_values(row_table, column)
    return new_dict


def head(column_based_table: dict[str, list[str]], num_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    new_dict: dict[str, list[str]] = {}
    for key in column_based_table:
        new_list: list[str] = []
        # print(key)
        i: int = 0
        while i < 5:
            new_list.append(column_based_table[key][i])
            i = i + 1
        new_dict[key] = new_list
    return new_dict
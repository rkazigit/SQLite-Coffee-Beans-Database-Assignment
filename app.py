import database

MENU_PROMPT = """ -- Coffee Bean App --

Please choose one of these options:

1) Add a new bean
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
"""

def menu():
    connection = database.connect()
    database.create_tables(connection)
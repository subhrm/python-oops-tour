import sqlite3

def setup_database(db_name:str):
    """
    Onetime database table setup
    """

    import sqlite3
    con = sqlite3.connect(db_name)

    cur = con.cursor()

    # Create table
    cur.execute('''CREATE TABLE fuel_details
                (location text, fuel_type text, price_per_liter real)''')

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()
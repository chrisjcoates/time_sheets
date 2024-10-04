import sqlite3


class Databse:

    def __init__(self, filepath):
        super().__init__()

        # Set filepath of database
        self.filepath = filepath

    def connect_to_database(self):
        # Create connection to database
        self.con = sqlite3.connect(self.filepath)

        # Create cursor
        self.cur = self.con.cursor()

    def insert_record(self, table, data):
        # Connect the database
        self.connect_to_database()

        # create list of '?' for value markers
        value_markers = []
        for i in data:
            value_markers.append("?")

        # Insert query
        query = f"INSERT INTO {table} VALUES ({', '.join(value_markers)})"

        # Execute and commit the query
        self.cur.executemany(query, data)
        self.con.commit()

        # Close the database connection
        self.con.close()

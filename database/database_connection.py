import sqlite3


class DatabaseConnection:

    def __init__(self, filepath=None, table=None, columns=None):
        super().__init__()

        # Set filepath of database
        self.filepath = filepath
        self.table = table
        self.columns = columns

    def connect_to_database(self):
        # Create connection to database
        self.con = sqlite3.connect(self.filepath)

        # Create cursor
        self.cur = self.con.cursor()

    def insert_record(self, data):
        # Connect the database
        self.connect_to_database()

        # create list of '?' for value markers
        value_markers = []
        for i in data:
            value_markers.append("?")

        markers = ", ".join(value_markers)
        columns = ", ".join(self.columns)

        # Insert query
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({markers})"
        print(query)

        # Execute and commit the query
        try:
            self.cur.execute(query, data)
        except sqlite3.Error as e:
            print(f"Some error occured {e}")
        finally:
            self.con.commit()

            # Close the database connection
            self.con.close()

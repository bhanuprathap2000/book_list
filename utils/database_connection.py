import sqlite3


# in order to make this a context manger __enter__ and __exit__ are required
class DatabaseConnection:
    # this will called when we create an instance of the class
    def __init__(self, host):
        self.connection = None
        self.host = host

    # this will called when we enter into the context manager
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    # this will called when we are exit out of the context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

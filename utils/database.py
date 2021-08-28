import sqlite3
from utils.database_connection import DatabaseConnection
from typing import List, Dict, Union

'''All operations in sqlite are performed by cursor and not by connection object itself This is because we can have 
one single collection and many cursor objects which can read data and at most one write operation at a time
 
 commit- save the result of the query to the disk 
 so until we say commit nothing is saved on the disk it is kept in the memory
 we can write multiple things together which is faster than individual writes
 
 type hinting
 since python is a dynamically typed language the variables are not bound to the data types
 this gives us flexibility but at the same time some drawback
 now the ide cannot suggest the what type the function expects or it returns 
 this is solved in python with type hinting
 for return values use ->type
 for parameters use :
 typing module
 
 this type hinting is very useful as the project grows a
 We need to add this just before :in functions and after the parameter name in function
 '''

# telling the pycharm the type of data to be returned.
Book = List[Dict[str, str, Union[str, int]]]


# now we have used the custom context manager database_connection


def create_book_table() -> None:
    # with open(books_file, 'w') as file:
    #     json.dump([], file)  # here file is the file object through which we can reference the file
    #     # initially json cannot be empty either it has to be [] or {} json module accepts [].

    # opening a database connection data.db will be created at the root of the file
    # connection = sqlite3.connect('data.db')  # a connection object is returned through which we can create cursor
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()  # creating a cursor we can create multiple cursor
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer )')  # using the cursor we can
        # execute the sql query


# here readline returns a list where each element is a string of that corresponding line
def get_all_books() -> Book:
    # with open(books_file, 'r') as file:
    #     return json.load(file)

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')  # cursor,execute executes the method and returns a result set to which
        # cursor points to the first row
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in
                 cursor.fetchall()]  # cursor.fetchall() return
        # data in [(),()] where each tuple is row  data since no saving here no need to commit.

    return books


def add_book(name:str, author:str)->None:
    # with open(books_file, 'a') as file:
    #     books = get_all_books()
    #     books.append({'name': name, 'author': author, 'read': False})
    #     _save_all_books(books)
    with DatabaseConnection(
            'data.db') as connection:  # a connection object is returned through which we can create cursor
        cursor = connection.cursor()  # creating a cursor we can create multiple cursor
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))  # using the cursor we can
        # execute the sql query


# this is a function starting with _ indicating that this should not be used by other programmers
# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         json.dump(books, file)


def mark_book_as_read(name:str)->None:
    # books = get_all_books()
    # for book in books:
    #     if book['name'] == name:
    #         book['read'] = True
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?',
                       (name,))  # we need to pass the placeholder as tuples so to avoid sql injection.


def delete_book(name:str)->None:
    # books = get_all_books()
    # books = [book for book in books if book['name'] != name]
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?',
                       (name,))  # we need to pass the placeholder as tuples so to avoid sql injection.

# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)

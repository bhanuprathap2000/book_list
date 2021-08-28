import sqlite3

'''All operations in sqlite are performed by cursor and not by connection object itself This is because we can have 
one single collection and many cursor objects which can read data and at most one write operation at a time
 
 commit- save the result of the query to the disk 
 so until we say commit nothing is saved on the disk it is kept in the memory
 we can write multiple things together which is faster than individual writes
 '''
books_file = 'books.json'


def create_book_table():
    # with open(books_file, 'w') as file:
    #     json.dump([], file)  # here file is the file object through which we can reference the file
    #     # initially json cannot be empty either it has to be [] or {} json module accepts [].

    # opening a database connection data.db will be created at the root of the file
    connection = sqlite3.connect('data.db')  # a connection object is returned through which we can create cursor
    cursor = connection.cursor()  # creating a cursor we can create multiple cursor
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer )')  # using the cursor we can
    # execute the sql query
    connection.commit()  # saving to the disk
    connection.close()  # closing the connection


# here readline returns a list where each element is a string of that corresponding line
def get_all_books():
    # with open(books_file, 'r') as file:
    #     return json.load(file)

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')  # cursor,execute executes the method and returns a result set to which
    # cursor points to the first row
    books = [{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()]  # cursor.fetchall() return
    # data in [(),()] where each tuple is row  data since no saving here no need to commit.
    connection.close()  # closing the connection
    return books


def add_book(name, author):
    # with open(books_file, 'a') as file:
    #     books = get_all_books()
    #     books.append({'name': name, 'author': author, 'read': False})
    #     _save_all_books(books)
    connection = sqlite3.connect('data.db')  # a connection object is returned through which we can create cursor
    cursor = connection.cursor()  # creating a cursor we can create multiple cursor
    cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))  # using the cursor we can
    # execute the sql query
    connection.commit()  # saving to the disk
    connection.close()  # closing the connection


# this is a function starting with _ indicating that this should not be used by other programmers
# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         json.dump(books, file)


def mark_book_as_read(name):
    # books = get_all_books()
    # for book in books:
    #     if book['name'] == name:
    #         book['read'] = True
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,)) # we need to pass the placeholder as tuples so to avoid sql injection.
    connection.commit()
    connection.close()

def delete_book(name):
    # books = get_all_books()
    # books = [book for book in books if book['name'] != name]
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?',(name,))  # we need to pass the placeholder as tuples so to avoid sql injection.
    connection.commit()
    connection.close()

# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)

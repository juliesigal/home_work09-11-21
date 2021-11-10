***** targil 1:
  
  
class Book:
    pass

def create_person(title, author, genre, year_of_publish, no_of_pages):
    my_book = Book()
    my_book.title = title
    my_book.author = author
    my_book.genre = genre
    my_book.year_of_publish = year_of_publish
    my_book.no_of_pages = no_of_pages
    return my_book


my_book = Book()
my_book.__dict__['title'] = 'Friends'
my_book.__dict__['author'] = 'Jonh Smith'
my_book.__dict__['genre'] = 'comedy'
my_book.__dict__['year_of_publish'] = '1993'
my_book.__dict__['no_of_pages'] = 1570

my_book = Book()
my_book.title = 'Friends'
my_book.author = 'Jonh Smith'
my_book.genre = 'comedy'
my_book.year_of_publish = 1993
my_book.no_of_pages = 1570



***** targil 4:
  
  
class Car:
    pass

my_car = Car
my_car.mark = 'Ford'
my_car.model = 'Mustang'
my_car.year = 1999
my_car.engine = 2500
my_car.color = 'grey'
print(my_car)  


class Car:
    def __init__(self) -> None:
        self.color = 'Red'
        self.make = "Mercedes"


class Elevator:
    # Class Constructor with atribute self
    # Is necesary pass self to any method with use a object instance reference
    def __init__(self, starting_floor) -> None:
        # atributes in teh constructor
        self.make = "The elevator company"
        self.floor = starting_floor


class Book:
    def __init__(self, author, title, pages, date_publish) -> None:
        self.author = author
        self.title = title
        self.pages = pages
        self.date_publish = date_publish


class Square:
    # use _atr (protected ) modificacion de acceso  __(private)
    def __init__(self,w,h):
        self.__height = h
        self.__width = w

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    # descriptores de accesso y mutadores  con propiedades
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Value needs to be 0 or larger")


# To create the objects
elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)


car = Car()
print(car.color)
print(car.make)  # result in an error, `make` does not exist on the object

book = Book(author="Jose Marti",
            title="Edad de Oro",
            pages=200,
            date_publish="1884")

square = Square()
square.__height = 3

from abc import ABC, abstractmethod
class Direction(ABC):
    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def backward(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

class NorthDirection(Direction):
    """ Classe per direzione N """
    def __init__(self) -> None:
        self.name = 'N'
        
    def __str__(self) -> str:
        return self.name

    def forward(self, x, y):
        return x, y+1

    def backward(self, x, y):
        return x, y-1

    def left(self):
        return WestDirection()

    def right(self) -> Direction:
        return EastDirection()
        
    

class EastDirection(Direction):
    """ Classe per direzione E """
    def __init__(self) -> None:
        self.name = 'E'
        
    def __str__(self) -> str:
        return self.name

    def forward(self, x, y):
        return x+1, y

    def backward(self, x, y):
        return x-1, y

    def left(self):
        return NorthDirection()

    def right(self):
        return SouthDirection()

class SouthDirection(Direction):
    """ Classe per direzione S """
    def __init__(self) -> None:
        self.name = 'S'
        
    def __str__(self) -> str:
        return self.name

    def forward(self, x, y):
        return x, y-1

    def backward(self, x, y):
        return x, y+1

    def left(self):
        return EastDirection()

    def right(self):
        return WestDirection()
    
class WestDirection(Direction):
    """ Classe per direzione W """
    def __init__(self) -> None:
        self.name = 'W'
        
    def __str__(self) -> str:
        return self.name

    def forward(self, x, y):
        return x-1,y

    def backward(self, x, y):
        return x+1, y

    def left(self):
        return SouthDirection()

    def right(self):
        return NorthDirection()
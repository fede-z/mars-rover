from Coordinates import Coordinates

class Mars:
    """"
        Classe che modella il pianeta Marte come una griglia 2D.
        In alcune coordinate possono essere presenti degli ostacoli.
    """
    def __init__(self, x: int, y: int, obstacles: list[Coordinates]):
        self.x = x
        self.y = y
        self.obstacles = obstacles

        self.__validate_mars()

    def __str__(self) -> str:
        string =  "Mars: gligia=" + str(self.x) + 'x'+ str(self.x) + ', ostacoli: '
        for o in self.obstacles:
            string += o.__str__() + " "
        return string
    
    def __validate_mars(self) -> None:
        """"
        Controlla la validità del pianeta Marte.
        """
        if not isinstance(self.x, int) or not isinstance(self.y, int) or not isinstance(self.obstacles, list):
            raise Exception("Uno o più parametri non corretti nel tipo.")
        if self.x < 0 or self.y < 0:
            raise Exception("Dimensioni griglia non valide, devono essere entrambe > 0.")
        for o in self.obstacles:
            if not self.on_surface(o):
                raise Exception("Coordinate degli ostacoli non valide.")

    def on_surface(self, coords:Coordinates) -> bool:
        """"
        Controlla se le coordinate coords risiedono sulla superficie del pianeta
        """
        return coords.x >= 0 and coords.x <= self.x and coords.y >= 0 and coords.y <= self.y
    
    def check_obstacles(self, coords:Coordinates) -> bool:
        """"
        Controlla se nelle coordinate coords è presente un ostacolo
        """
        x = coords.x
        y = coords.y
        for o in self.obstacles:
            if o.x == x and o.y == y:
                return True
        return False

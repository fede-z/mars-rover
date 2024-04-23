class Coordinates:
    """"
        Classe che modella le coordinate cartesiane X,Y
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.__validate_coords(self.x,self.y)

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def set_x(self, x):
        """ Aggiorna coordinata x se valida"""
        self.__validate_coords(x, self.y)
        self.x = x

    def set_y(self, y):
        """ Aggiorna coordinata y se valida"""
        self.__validate_coords(self.x, y)
        self.y = y

    def __validate_coords(self, x, y):
        """ Controlla che entrambe le coordinate siano numeri interi"""
        if not isinstance(x, int) or not isinstance(y, int):
            raise Exception("Coordinate non numeriche")
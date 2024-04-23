from Coordinates import Coordinates
from Direction import Direction
from Mars import Mars

class Rover:
    """"
        Classe che modella un rover posizionato nelle coordinate 'coortinates' e con direzione 'direction'
        sul pianeta 'mars'
    """

    def __init__(self, coordinates: Coordinates, direction:Direction, mars:Mars):
        self.coortinates = coordinates
        self.direction = direction
        self.mars = mars

        self.__validate_rover()

    def execute(self, commands: list):
        """
        Esegue la lista di comandi passata come parametro
        """
        self.__validate_commands(commands)
        for c in commands:
            print(c)
            new_x = self.coortinates.x
            new_y = self.coortinates.y
            new_dir = self.direction

            if c == 'F':
                new_x, new_y = self.direction.forward(self.coortinates.x, self.coortinates.y)

            if c == 'B':
                new_x, new_y = self.direction.backward(self.coortinates.x, self.coortinates.y)

            if c == 'L':
                new_dir = self.direction.left()

            if c == 'R':
                new_dir = self.direction.right()

            new_x, new_y = self.__wrap_around(new_x, new_y)
            
            if self.mars.check_obstacles(Coordinates(new_x,new_y)):
                print("E' presente un ostacolo, sequenza interrotta.")
                return

            self.__set_rover_position(new_x, new_y, new_dir)

    def __wrap_around(self, x, y):
        """
        Sistemo coordinate x e y nel caso in cui escano dalla griglia (wrap-around). 
        Il rover deve ricomparire nel lato opposto della griglia.
        """
        new_x = x  % self.mars.x
        new_y = y % self.mars.y
        return new_x, new_y
    
    def __validate_rover(self):
        """
        Valida il rover: deve avere coordinate valide per il pianeta e non essere posizionato su un ostacolo.
        """
        if not isinstance(self.coortinates, Coordinates) or not isinstance(self.direction, Direction) or not isinstance(self.mars, Mars):
            raise Exception('Uno o più parametri non corretti nel tipo')
        if not self.mars.on_surface(self.coortinates):
            raise Exception('Rover non sulla superficie del pianeta')
        if self.mars.check_obstacles(self.coortinates):
            raise Exception('Non è possibile posizionare il rover su uno ostacolo')
        
        
    def __validate_commands(self, commands):
        """
        Valida la lista di comandi 'commands'
        Devono essere F, B, L o R
        """
        for c in commands:
            if c not in ['F', 'B', 'L', 'R']:
                raise Exception('Sequenza di comandi non valida')
        
    def __validate_position(self, x, y, direction):
        """
        Valida x, y e direction
        """
        c = Coordinates(x,y)
        return not self.mars.check_obstacles(c) and isinstance(direction, Direction) and self.mars.on_surface(c)

    def get_rover_x(self):
        """
        Restituisce la cordinata x del rover.
        """
        return self.coortinates.x
    
    def get_rover_y(self):
        """
        Restituisce la cordinata y del rover.
        """
        return self.coortinates.y
    
    def __set_rover_position(self, x, y, direction):
        """
        Aggiorna la posizione del rover (coordinate + direzione) se valida.
        """
        if self.__validate_position(x, y, direction):
            print('New position:', x, y, direction)
            self.coortinates.set_x(x)
            self.coortinates.set_y(y)
            self.direction = direction
    
    def get_rover_position(self):
        """
        Restituisce una stringa con la posizione del rover (coordinate + direzione).
        """
        return "Rover in " + self.coortinates.__str__() + " direzione " + self.direction.__str__()

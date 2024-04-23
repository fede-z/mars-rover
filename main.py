from Coordinates import Coordinates
from Direction import *
from Mars import Mars
from Rover import Rover

def set_direction(dir):
    """Ritorna l'oggetto Direction corrispondente a dir."""
    if dir == 'N':
        return NorthDirection()
    if dir == 'E':
        return EastDirection()
    if dir == 'W':
        return WestDirection()
    if dir == 'S':
        return SouthDirection()
    else: 
        raise Exception('Direzione non valida')
if __name__ == '__main__':
    try : 
        with open('input.txt', 'r') as file:
            lines = file.readlines()


        mars_x, mars_y = map(int, lines[0].split())
        obstacles = []
        if lines[1] != "\n":
            obs = lines[1].split(';')
            for o in obs:
                x, y = map(int, o.split())
                obstacles.append(Coordinates(x,y))

        mars = Mars(mars_x,mars_y, obstacles)
        print(mars.__str__())

        rover_x, rover_y, rover_dir = lines[2].split()
        direction = set_direction(rover_dir)
        rover_x = int(rover_x)
        rover_y = int(rover_y)

        commands = []
        if lines[3] != "\n":
            commands = list(lines[3].split()[0])

        rover = Rover(Coordinates(rover_x,rover_y),direction,mars)
        print(rover.get_rover_position())
        print('Comandi:',commands)

        rover.execute(commands)
        
        print(rover.get_rover_position())

    except Exception as e:
        print('Possibile file input formattato male.')
        print('Errore:', e)
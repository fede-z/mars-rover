from Direction import *
from Mars import Mars
from Rover import Rover
from Coordinates import Coordinates
import unittest

class testCoordinates(unittest.TestCase):
    """ Classe di test per la classe Coordinates. """
    def test_bad_x(self):
        with self.assertRaises(Exception):
            c = Coordinates(x='1',y=3)

    def test_bad_y(self):
        with self.assertRaises(Exception):
            c = Coordinates(x=1,y=3.7)

    def test_bad_coords(self):
        with self.assertRaises(Exception):
            c = Coordinates(x='1',y='3')

    def test_bad_set_x(self):
        """ Solo coordinate intere """
        c = Coordinates(x=1,y=3)
        with self.assertRaises(Exception):
            c.set_x('3')

    def test_bad_set_y(self):
        """ Solo coordinate intere """
        c = Coordinates(x=1,y=3)
        with self.assertRaises(Exception):
            c.set_y(3.5)

class testDirection(unittest.TestCase):
    """ Classe di test per le classi Direction. """
    def test_north_direction(self):
        """ testa NorthDirection """
        dir = NorthDirection()
        x,y = dir.forward(x=1,y=1)
        self.assertEqual(y, 2)
        x,y = dir.backward(x=x,y=y)
        self.assertEqual(y, 1)
        self.assertIsInstance(dir.left(), WestDirection)
        self.assertIsInstance(dir.right(), EastDirection)

    def test_east_direction(self):
        """ testa EastDirection """
        dir = EastDirection()
        x,y = dir.forward(x=1,y=1)
        self.assertEqual(x, 2)
        x,y = dir.backward(x=x,y=y)
        self.assertEqual(x, 1)
        self.assertIsInstance(dir.left(), NorthDirection)
        self.assertIsInstance(dir.right(), SouthDirection)

    def test_south_direction(self):
        """ testa SouthDirection """
        dir = SouthDirection()
        x,y = dir.forward(x=1,y=1)
        self.assertEqual(y, 0)
        x,y = dir.backward(x=x,y=y)
        self.assertEqual(y, 1)
        self.assertIsInstance(dir.left(), EastDirection)
        self.assertIsInstance(dir.right(), WestDirection)

    def test_west_direction(self):
        """ testa WestDirection """
        dir = WestDirection()
        x,y = dir.forward(x=1,y=1)
        self.assertEqual(x, 0)
        x,y = dir.backward(x=x,y=y)
        self.assertEqual(x, 1)
        self.assertIsInstance(dir.left(), SouthDirection)
        self.assertIsInstance(dir.right(), NorthDirection)


class testMars(unittest.TestCase):
    """ Classe di test per la classe Mars. """
    def test_bad_mars_grid(self):
        """ Le dimensioni di x e y della griglia devono essere valide (>0)"""
        with self.assertRaises(Exception):
            mars = Mars(-10, 10,[Coordinates(1,2)])

    def test_bad_mars_coords(self):
        """ Le coordinate degli ostacoli devono essere valide"""
        with self.assertRaises(Exception):
            mars = Mars(10, 10,[Coordinates(-10,-10)])

    def test_on_surface1(self):
        """ on_surface ritorna False se le coordinate in input non sono valide per mars"""
        mars = Mars(10, 10, obstacles=[])
        result = mars.on_surface(Coordinates(11,11))
        self.assertFalse(result)

    def test_on_surface2(self):
        """ on_surface ritorna True se le coordinate in input sono valide per mars"""
        mars = Mars(x=10, y=10, obstacles=[])
        result = mars.on_surface(Coordinates(9,2))
        self.assertTrue(result)

    def test_check_obstacles(self):
        """ check_obstacles ritorna False se le coordinate in input non coincidono con nessun un ostacolo"""
        mars = Mars(x=10, y=10, obstacles=[])
        result = mars.check_obstacles(Coordinates(9,2))
        self.assertFalse(result)

    def test_check_obstacles2(self):
        """ check_obstacles ritorna True se le coordinate in input coincidono con almeno un ostacolo"""
        mars = Mars(x=10, y=10, obstacles=[Coordinates(9,2)])
        result = mars.check_obstacles(Coordinates(9,2))
        self.assertTrue(result)


class testRover(unittest.TestCase):
    """ Classe di test per la classe Rover. """

    def test_bad_rover_coords(self):
        """ Il rover deve risiedere nella griglia di marte """
        mars = Mars(x=10, y=10, obstacles=[])
        with self.assertRaises(Exception):
            mars = Rover(Coordinates(-1,2), NorthDirection(), mars)

    def test_bad_rover_direction(self):
        """ Il rover deve avere direzione iniziale Direction """
        mars = Mars(x=10, y=10, obstacles=[])
        with self.assertRaises(Exception):
            mars = Rover(Coordinates(1,2), 'N', mars)

    def test_rover_execute(self):
        """ Lista vuota di comandi non altera la posizione del rover """
        mars = Mars(x=10, y=10, obstacles=[])
        rover = Rover(Coordinates(0,0), NorthDirection(), mars)
        position1 = rover.get_rover_position()
        rover.execute([])
        position2 = rover.get_rover_position()
        self.assertEqual(position1, position2)

    def test_rover_execute2(self):
        """ Accetta comandi F, B, L, R """
        mars = Mars(x=10, y=10, obstacles=[])
        rover = Rover(Coordinates(0,0), NorthDirection(), mars)
        for c in ['F', 'B', 'L', 'R']:
            result = rover.execute([c])
            self.assertIsNone(result)

    def test_rover_execute2(self):
        """ Comportamento wrap-around """
        mars = Mars(x=10, y=10, obstacles=[])
        rover = Rover(Coordinates(0,0), SouthDirection(), mars)
        c = ['F', 'F', 'F', 'F']
        result = rover.execute(c)
        self.assertIs(rover.coortinates.y, 6)

    def test_bad_rover_execute(self):
        """ Non accetta comandi diversi da F, B, L, R """
        mars = Mars(x=10, y=10, obstacles=[])
        rover = Rover(Coordinates(0,0), NorthDirection(), mars)
        with self.assertRaises(Exception):
            result = rover.execute(['S'])


if __name__ == '__main__':
    unittest.main()



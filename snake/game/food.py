import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here

class Food(Actor):
    """ The responsibility of Food is to keep track of its appearance and position. Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder


    Attributes: 
        _points (integer): The number of points the food is worth.
        
        """
    
    def __init__(self):
        """ Class constructor

            Args:

            _points (int): stores the count of points for the food
        
        """
        super().__init__()
        self._points = 0
        self.set_text('@')
        self.reset()


    def get_points(self):
        """ Method that returns the points """
        return self._points
    
    def set_points(self, points):
        """ Method that sets the new points """
        self._points = points
        
    def reset(self):
        """ Description here """    
        new_points = random.randint(1, 5)
        self.set_points(new_points)

        x = random.randint(1, constants.MAX_X - 1)
        y = random.randint(1, constants.MAX_Y - 1)
        position = Point(x, y)
        self.set_position(position)


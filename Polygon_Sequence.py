from functools import lru_cache
from Polygon import Polygon


class Polygon_Sequence:
    """Implementaion Of Custom Sequence of Polygons which takes largest \
        polygon num of edges and circumradius as input"""

    def __init__(self, num_edges: int, circumradius: float) -> None:
        """ Function initialising the number of edges and circumradius"""
        self.largest_num_edges = num_edges
        self.circumradius = circumradius

    def __repr__(self):
        """Repr Function to print regarding the initialized variables"""
        return f'Polygon Sequence::  Circumradius : {self.circumradius} , Largest Number Of Edges: {self.largest_num_edges}, length : {self.__len__()}'

    @property
    def largest_num_edges(self):
        """Function to return the largest number of edges"""
        return self._largest_num_edges

    @largest_num_edges.setter
    def largest_num_edges(self, value):
        """Function setting the largest number of edges"""
        if value < 3:
            raise ValueError("The number of vertices should be more than 3")
        self._largest_num_edges = value

    @property
    def circumradius(self):
        """Function to return the circumradius"""
        return self._circumradius

    @circumradius.setter
    def circumradius(self, value):
        """Function to set the circumradius"""
        if(value < 0):
            raise ValueError(" Radius should be greater than 0")
        self._circumradius = value

    def __len__(self):
        """Function returning the length of sequence"""
        return self.largest_num_edges - 2

    def __getitem__(self, pos):
        """Function to retrieve a particular element in the sequence or a \
            list of elements"""

        if isinstance(pos, int):
            if pos < 0:
                pos = self.largest_num_edges - 2 + pos
            if pos < 0 or pos >= (self.largest_num_edges - 2):
                raise IndexError
            else:
                return self._polygon(pos + 3)
        else:
            start, stop, step = pos.indices(self.largest_num_edges-2)
            rng = range(start, stop, step)
            return [self._polygon(i+3) for i in rng]

    @lru_cache(512)
    def _polygon(self, num_edges):
        """Function returning a polygon of particular num of edges and \
            circumradius along with all the properties"""
        return Polygon(num_edges, self.circumradius)

    @property
    @lru_cache(1)
    def max_efficiency_polygon(self):
        """Function returning the max efficiency calculated according to the \
            formulae"""
        return sorted(self, key=lambda polygon: polygon.area/polygon.perimeter)[-1]

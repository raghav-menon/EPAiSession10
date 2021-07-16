from Polygon import *
from Polygon_Sequence import *
import Polygon as Polygon
import Polygon_Sequence as Polygon_Sequence
from datetime import datetime, date
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re
from decimal import Decimal

fake = Faker()

README_CONTENT_CHECK_FOR = [ '__init__', 
                            'num_edges',
                            'num_vertices',
                             'circumradius',
                             'interior_angle',
                             'edge_length',
                             'apothem', 
                             'area', 
                             'perimeter',
                             ' __repr__', 
                             '__eq__', 
                             '__gt__',
                             'largest_num_edges',
                             '__len__', 
                             '__getitem__', 
                             '_polygon', 
                             'max_efficiency_polygon']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Polygon_Sequence)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_indentations_polygon():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Polygon_Sequence, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_polygon():
    functions = inspect.getmembers(Polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_len_sequence():
    N = 30
    C = 13
    ps = Polygon_Sequence.Polygon_Sequence(N,C)
    assert len(ps) == 28, 'Check the program'
    
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
    
def test_max_efficiency():
    N = 25
    C = 10
    ps = Polygon_Sequence.Polygon_Sequence(N,C)
    with Capturing() as output:
        print(ps.max_efficiency_polygon)
    
    assert any([str(N) in o.split() for o in output]), ' Check the program'
    
def test_check_equal():
    p1 = Polygon.Polygon(10,25)
    p2 = Polygon.Polygon(10,25)
    p3 = Polygon.Polygon(11,25)
    
    assert p1 == p2, 'Check program'
    assert p1 != p3, ' Check program'
    
def test_check_gt():
    p1 = Polygon.Polygon(10,25)
    p2 = Polygon.Polygon(11,26)
    p3 = Polygon.Polygon(11,25)
    
    assert p1<p2, 'Check program'
    assert p1<p3, 'Check program'
    
def test_check_area():
    p1 = Polygon.Polygon(10,10)
    
    assert p1.area > 0, 'Check program'

    
    

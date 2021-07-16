## Session 10 - Sequence Types I

## Assignment Questions

** A regular strictly convex polygon is a polygon that has the following characteristics:**
1. all interior angles are less than 180
2. all sides have equal length
 
**For a regular strictly convex polygon with:**
* n edges (=n vertices)
* R circumradius
* interiorAngle=(n−2)⋅180n
* edgeLength,s=2⋅R⋅sin(πn)
* apothem,a=R⋅cos(πn)
* area=12⋅n⋅s⋅a
* perimeter=n⋅s

** Objective 1 **

1. Create a Polygon Class: where initializer takes in:
    * number of edges/vertices
    * circumradius

    that can provide these properties:
    * edges
    * vertices
    * interior angle
    * edge length
    * apothem
    * area
    * perimeter
    
    that has these functionalities:
    * a proper __repr__ function
    * implements equality (==) based on # vertices and circumradius (__eq__)
    * implements > based on number of vertices only (__gt__)
    
** Objective 2 **

1. Implement a Custom Polygon sequence type:where initializer takes in:

    * number of vertices for largest polygon in the sequence
    * common circumradius for all polygons

   that can provide these properties:
   
   * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
   
   that has these functionalities:
   * functions as a sequence type (__getitem__)
   * supports the len() function (__len__)
   * has a proper representation (__repr__)
   
2. Results:
    1. Implement these 2 classes as a separate module. Access these modules in a jupyter-notebook (or Google Colab or Deep Note)
    2. Run Objective 1 module to show that the functionalities are implemented properly
    3. Run Objective 2 module and show which polygon is efficient for n = 25
    4. You are submitting link to your GitHub repo, where we can find the 2 modules and your notebook in which you have called and tested them


## Class Polygon 

Implementation of a regular Polygon which takes num_eges and circumradius as input. It can give num_eges, num_vertices,interior angle, edge length,
apothem, area, perimeter

**Usage**

```python
p = Polygon(10, 10) # no of edges , circumradius
p.num_edges
p.perimeter
p.area

```

### __init__ 
This function initializes the number of edges and the circumradius to the polygon class.

### num_edges
This function returns the number of edges. This is decorated as class property. Also decorated with num_edges.setter, it helps to set the edges values.

## num_vertices
This function returns the number of edges. This is decorated as class property. Also decorated with num_vertices.setter, it helps to set the edges values.
For a regular polygon, the number of edges is equal to the number of vertices.

## circumradius
This function returns the circumradius. This is decorated as class property. Also decorated with circumradius.setter, it helps to set the circumradius
value.

## interior_angle
This function calculates the interior angle in accordance to the equation. This is decorated as class property.

## edge_length
This function calculates the edge length in accordance to the equation. This is decorated as class property.

## apothem
This function calculates the apothem in accordance to the equation. This is decorated as class property.

## area
This function calculates the area in accordance to the equation. This is decorated as class property.

## perimeter
This function calculates the perimeter in accordance to the equation. This is decorated as class property.

## __repr__
This function returns the property of the Polygon class initialized

## __eq__
Equality function to compare whether 2 polygons are equal by comparing the number of edges and circumradius

## __gt__
Greater than function to compare whether which of the 2 polygons is bigger by comparing the number of vertices


## Class Polygon_Sequence
Implementaion Of Custom Sequence of Polygons which takes largest polygon num of edges and circumradius as input

**Usage**

```python
p = Polygon_Sequence(num_edges = 10,  circumradius = 10) 

#for getting the each Polygon through index
p[3]

#slicing
p[3:10]

#length
len(p)

#max efficinecy polygon
p.max_efficiency_polygon


```

### __init__ 
This function initializes the largest number of edges and the circumradius to the polygon sequence class. The polygon sequence class generates a sequence of 
polygons greater than 2 upto the polygon with the largest number of edges

### largest_num_edges
This function returns the largest number of edges. This is decorated as class property. Also decorated with largest_num_edges.setter, it helps to set the 
largest number of edges values.

## circumradius
This function returns the circumradius. This is decorated as class property. Also decorated with circumradius.setter, it helps to set the circumradius
value.

## __repr__
This function returns the property of the Polygon sequence class initialized.

## __len__
This function provides the length of polygon sequence.

## __getitem__
This function helps to retrieve a particular value from the polygon sequence or a slice of values.

## _polygon
Calls the polygon class to get the properties

## max_efficiency_polygon
Caculates the maximum efficiency polygon

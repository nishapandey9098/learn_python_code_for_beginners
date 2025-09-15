coordinates = (10.0, 20.0)
print(coordinates)  
print(coordinates[0])
print(coordinates[1])       
# coordinates[0] = 1.0  # This will raise an error because tuples are immutable
x, y = coordinates  
print(x)
print(y)        
# Unpacking a tuple into variables  
coordinates2 = [(1, 2), (3, 4), (5, 6)]
print(coordinates2) 
print(coordinates2[0])
print(coordinates2[1])      
print(coordinates2[2])
print(coordinates2[0][0])   
print(coordinates2[0][1])
print(coordinates2[1][0])
print(coordinates2[1][1])
print(coordinates2[2][0])           
print(coordinates2[2][1])
for coordinate in coordinates2:
    print(coordinate)
# Nested tuples and accessing their elements
for (x, y) in coordinates2:
    print(x)
    print(y)
# Unpacking nested tuples in a loop
def add_coordinates(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])
result = add_coordinates((1, 2), (3, 4))
print(result)
print(result[0])
print(result[1])
# Function that takes tuples as arguments and returns a tuple
def swap(a, b):
    return (b, a)
swapped = swap(5, 10)           
print(swapped)
print(swapped[0])       
print(swapped[1])
# Function that swaps two values using tuples   
def min_max(numbers):
    return (min(numbers), max(numbers)) 
result = min_max([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(result)
print(result[0])

print(result[1])
# Function that returns the minimum and maximum of a list as a tuple
def create_point(x, y):
    return (x, y)
point = create_point(7, 8)
print(point)

    
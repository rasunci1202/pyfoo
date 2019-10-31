import numpy

my_list_of_tuples = [
    ('a', 'b', 1, 2),
    ('c', 'd', 3, 4),
    ('e', 'f', 5, 6),
    ]

print(my_list_of_tuples)
my_xs = [v3 for v1, v2, v3, v4 in list(my_list_of_tuples)]
print(my_xs)  

my_xs2 = [x[2] for x in list(my_list_of_tuples)]
print(my_xs2)  

my_cities = [
    ('Alhambra', 'USA', 34.097220, -118.126567),
    ('Catalina', 'USA', 33.395225, -118.416478),
    ('Long Beach', 'USA', 33.758529, -118.190804),
    ('Santa Monica', 'USA', 34.021868, -118.471286)
    ]

my_xs3 = [[x[2],x[3]] for x in list(my_cities)]
print(my_xs3)  

#my_col = [x] for x in list(my_list_of_tuples[2])
#print(my_col)


# Floyd-s-Algorithm-
This repository was created as for the mid-module assignment of CSCK 541.



Mid_Modul_Assignemnt: Code descrption 
Line 1-6: 
Code introduction as well as reference and credit to sources utilized. 
Line 7-13: 
The sys library was imported to make use of the .maxsize method. This allowed us to define infinity  or the situation where the distance between the nodes was non-existent. In addition nv was declared to indicate the number of vertices or nodes. This was made static at 4 as per the assignment instructions and dimensions of the input matrix. INF was used a variable stand-in for output of the sys.maxsize out. 
Line 14-24:
 The main algorithm called Floyd was defined here. The docstring for the function was also implemented using the PEP-8 Standard. 
Line 25-27:
 Distance between nodes is created here using a recursive function. 
1.	The variable dist is created to hold the output. 
2.	The variable is defined as a list 
3.	The map iterator is used to apply a function to every item in list iterable
4.	Within the map iterator is two nested lamba functions, one for p and q which then reads in the columns and rows on in the input matrix. The input matrix is then mapped to dist 
Line 28 – 33: 
Three nested for loops are then called which use the search space created by the nv (ma-trix dimension) variable to loop through the input matrix (dist) 
The dist list is then modified iteratively by using the min function which finds the min dis-tance between nodes. The nv variable limits the number of steps to 4 ensuring the there arnt an infinite amount of dimensioned searched. nv is parsed to variable r which is used in this loop. 
The dist list in now updated with the min distances.
List 34-55: 
A new function called sol defined to print the output of the floyd algorithm.
A docstring was written for this simple function. 
The sol function steps through the dist nested list. Variables p and q are again used to defined the column and rows respectively. 
Two nested for statements are used to loop through the elements within the list. 
INF is defined as a dedicated print statement provided for those items which are equal to the max system size. This is used for ease of reading the output. 
New line print points are included to pad the printed output for ease of reading and dis-play the output as a matrix instead of linear string of characters. 
Line 56 – 65: 
G and H are defined here. There are input matrixes to implement in the floyd algorithm and are hard coded. 
G and H are both 4 x 4 embedded list type variables.
G is defined as the input matrix from the assignment instruction which is also used in the original floyd algorithm script described above.
H was as input matrix with a known correct output from (Shivali Bhadaniya, 2022). This is used as a manual unit test to validate that the function. 
Line 65-70:
These lines were used as the wrapped to parse the input matrixes (assignment and man-ual unit test) as well as print the output the to terminal


# Turing-Python
Turing Python test

##First test

 * Reaching permutation

'''given an array of N integers, your task is to transform this array into a permutation of the first N positive intefers. A permutation of size N is an arrangement of numbers such that each numer from 1 to n appears exactly once.
in one operation, you canc increase or decrease any element of the array by 1

the challenge is to figure out the smalles number operations required to convert the given array

examples:

1. Input N = [3,2,1,4]
output: 0
explanation: no operation needed, already a permutation

2.Input N = [4,1,4,2]
output: 1
explanation: decrease one '4' to '3' to form the permutation [4,1,3,2]

contraints:
-the integers in the array N will be equal or bigger than 1
-the size of the array N can range from 1 to 10^5'''

##Second test

  * Frog Feast

There are several frogs on a line, each with an intefer coodinate and a specific tongue size. More precisely the Ith frog is on the
coordinate x, and its tongye has sise S.
Additionally, there are flies, also positioned on integer coordinates. the ith fly is positioned on the Y coordinate.
A frog i manages to eat a fly, and only if:

This means that the frog can eat the fly in distance between them is less than or equal to the size of the frog's tongue. Your task
is to determinate, for each frog, how many flies it can eat.

Input Format:
- X is a list of integers where X[i] representes the position of the ith frog.
- S is a list of integers where S[i] representes the size of the tongue of the ith frog.
- Y is a list of integers where Y[i] representes the position of the ith fly.

Out Format
- The function should return a list of integers where the ith intefer represents the number of the flies the ith frog can eat.

Examples: 
1. Input X = [1,4,5], S = [2,3,5], Y = [2,3,5]
Output: [2,3,3]

2. Input X = [3], S=[5], Y= [7,1,2,6,4,5,3,0,8]
Output: [9]

Contraints:
- Positions X[i], S[i] and Y[i] are non-negative intefers.
- no two frogs share the same position in the list X
- There mayy be cases where there are no frogs and/or no flies.
- 0 >= X, S & Y <=10^5.
 


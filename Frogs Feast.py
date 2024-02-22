'''Frog Feast

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
''' 

from typing import List

def frogs(X: List[int], S: List[int], Y: List[int]) -> List[int]:
    result = []
    
    for i in range(len(X)):
        current_frog_position = X[i]
        current_frog_tongue_size = S[i]
        
        # Initialize a counter for the number of flies the current frog can eat
        flies_eaten = 0
        
        for j in range(len(Y)):
            current_fly_position = Y[j]
            
            # Check if the distance between the frog and the fly is less than or equal to the tongue size
            if abs(current_frog_position - current_fly_position) <= current_frog_tongue_size:
                flies_eaten += 1
        
        result.append(flies_eaten)
    return result

#README
#DO NOT CHANGE THE CODE BELOW, WE USE IT TO GRADE YOUR SUBMISSION

if __name__ == '__main__':
    line = input()
    x = [int(i) for i in line.strip().split()]
    line = input()
    s = [int(i) for i in line.strip().split()]
    line = input()
    y = [int(i) for i in line.strip().split()]
    output = frogs(x, s, y)
    if output == []:
        print('[]')
    else:
        print('[%s]' % ','.join(map(str, output)))
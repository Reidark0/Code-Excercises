'''Let's learn about list comprehensions! 
You are given three integers x, y and z representing the dimensions 
of a cuboid along with an integer n. Print a list of all possible coordinates 
given by (i, j , k) on a 3D grid where the sum of i + j + k is not equal to n. Here,
0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 
Please use list comprehensions rather than multiple loops, as a learning exercise.'''

# need to create various lists with the permutation of x, y and z

#if __name__ == '__main__':
x = int(input())
y = int(input())
z = int(input())
n = int(input())
a = [x, y, z]
newA = [letra for letra in a if letra == 1 in a ]
4
for i in range(4):
    print('d')
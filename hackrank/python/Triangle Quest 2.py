'''You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.
More than 2 lines will result in 0 score. Do not leave a blank line also'''


'''Wrong Answer = str is not allowed'''
for i in range(1,int(input())+1):  
    print (''.join([str (a) for a in (range(1,i+1))]),''.join([str (a) for a in (reversed(range(1,i)))]), sep='')


'''Wrong Answer = only 1 for is allowed'''
for i in range(1,int(input())+1):
    print (*[a for a in (range(1,i+1))],*[a for a in (reversed(range(1,i)))], sep='')


'''Wrong Answer = invalid string literal found'''
for i in range(1,int(input())+1):
    print (*range(1,i+1),*reversed(range(1,i)), sep='')


'''Using Math because i cant figure out a way to remove the white spaces withou using str'''
'''Wrong Answer = more than two lines of code is not allowed'''
for i in range(1,int(input())+1):
     a = 1
     i -= 1
     while i>=1:
        a += 10**i
        i -= 1
     print(a**2)
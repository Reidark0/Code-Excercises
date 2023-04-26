'''The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.'''

if __name__ == '__main__':
    n = int(input())
    a = range(1,n+1)
    l = ''
    for i in a:
        l = l+str(i)
    print(l)

''' OU '''

if __name__ == '__main__':
    n = int(input())
    a = range(1,n+1)
    print(''.join(str(e) for e in list(a)))

''' OU '''

if __name__ == '__main__':
    n = int(input())
    print(''.join([str(i) for i in range(1,n+1)]))

# Write a function, persistence, that takes in a positive parameter num and 
# returns its multiplicative persistence, which is the number of times you 
# must multiply the digits in num until you reach a single digit.

def persistence(num):
    resposta = 0
    while len(str(a)) >= 2:
        b = []
        resposta +=1
        for i in str(a):
            b.append(int(i))
        c = 1
        for i in b:
            c = i * c
        a = c
    return resposta
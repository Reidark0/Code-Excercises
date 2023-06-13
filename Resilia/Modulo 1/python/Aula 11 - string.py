a = 'Hoje eu quero quebrar alguem'
b = a[::-1]
print(b)
a = a.lower()
for i in range(len(a)):
    print(a[::-1][i])

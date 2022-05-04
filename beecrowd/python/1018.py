'''
Banknotes
'''
i = int(input())
cem = 0
cinq = 0
vint = 0
dez = 0
cinc = 0
dois = 0
um = 0
d = i
while d >= 100:
    d -= 100
    cem += 1
while d >= 50:
    d -= 50
    cinq += 1
while d >= 20:
    d -= 20
    vint += 1
while d >= 10:
    d -= 10
    dez += 1
while d >= 5:
    d -= 5
    cinc += 1
while d >= 2:
    d -= 2
    dois += 1
while d >= 1:
    d -= 1
    um += 1

print(f"{i}\n{cem} nota(s) de R$ 100,00\n"
      f"{cinq} nota(s) de R$ 50,00\n"
      f"{vint} nota(s) de R$ 20,00\n"
      f"{dez} nota(s) de R$ 10,00\n"
      f"{cinc} nota(s) de R$ 5,00\n"
      f"{dois} nota(s) de R$ 2,00\n"
      f"{um} nota(s) de R$ 1,00")
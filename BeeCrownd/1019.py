'''
Time Conversion
'''
segundos = int(input())

CAUCLULO_1 = int(segundos/3600)
CAUCLULO_2 = int(segundos%3600/60)
CAUCLULO_3 = int(segundos%60)

print(f'{CAUCLULO_1}:{CAUCLULO_2}:{CAUCLULO_3}')
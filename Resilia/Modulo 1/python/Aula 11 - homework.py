str = 'X-DSPAM-Confidence:0.8475'

# separa tudo depois dos : usando find e fatiamento de string

a = str.find(':')
b = str[a + 1:]
b = float(b) * 100
print(b)
'''
aba = 5
b = 2
print(aba ** b)

for i in range(0, 10, 2):
    if (5 > 1):
        print ('Hello world!', i)
    else:
        print('Goodbue') 
'''
'''
s = "Artem and 111 and hello"
a = s.split('d')
print('a'.join(a))
'''
for i in range(1000, 10000):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    s1 = first + second
    if s1 == '1215':
        print(i)
        break

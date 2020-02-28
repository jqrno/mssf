def funcao(t):
    return (2*(t**3)) - (10*(t**2)) - (30*t) + 50

print('-----------------')
print('|   t   |  x(t) |')
print('-----------------')
for t in range(11):
    print('|   {}   |   {}   |'.format(t, funcao(t)))
    print('-----------------')
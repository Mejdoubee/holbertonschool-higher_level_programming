#!/usr/bin/python3
'''
for i in range(90, 64, -1):
    if i % 2 == 0:
        i += 32
    print("{}".format(chr(i)), end="")
'''
print(end='{}'.format(''.join(map(
    lambda x: chr(x + 32) if x % 2 == 0 else chr(x),
    range(90, 64, -1)))))

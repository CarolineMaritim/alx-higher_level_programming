#!/usr/bin/python3

index = 0

for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char)), end="")
    i = 32 if i == 0 else 0

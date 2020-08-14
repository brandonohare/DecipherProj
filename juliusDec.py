#!/usr/bin/python

import base64

def split(w):
    return [char for char in w]

def mainTWO():
    cipher = raw_input()
    cipher = base64.b64decode(cipher)
    cipher = split(cipher)

    for i in range(0, len(cipher)):
        cipher[i] = format(ord(cipher[i]), "x")

    for j in range(0, 255):
        num = hex(j)
        num = num[2:]
        print num
        text = ""
        arr = [None] * len(cipher)
        
        for i in range(0, len(cipher)):
            arr[i] = hex(int(cipher[i], base=16) ^ int(num, base=16))
            arr[i] = arr[i][2:]
            text += arr[i]
        
        if len(text) % 2 != 0:
            text = text[1:]
        print text.decode("hex")
        print "Key ^:", num

mainTWO()
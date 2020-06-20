import random

def PseudoRandomText():
    text = ''
    for i in range(20):
        num = random.randint(35, 120)
        char = chr(num)
        text += char
    return text


words = open('words.txt', 'w')
for i in range(1000):
    words.write(f"{PseudoRandomText()} \n")

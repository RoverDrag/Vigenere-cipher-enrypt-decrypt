def v_encrypt(key):
    data = list(str(input()))
    def newsymb(letter,k):
        if letter.isupper():
            return chr((ord(letter) + k - 65) % 26 + 65)
        else:
            return chr((ord(letter) + k - 97) % 26 + 97)
    ckey = 0
    for i in range(len(data)):
        if data[i].isalpha():
            data[i] = newsymb(data[i],ord(key[ckey]) - 97)
            ckey += 1
            if ckey == len(key):
                ckey = 0
    return ''.join(data)
print(v_encrypt('pizza'))
import base64, promptAi

def b64String(text):
    text_bytes = text.encode("ascii")
    b64_bytes = base64.b64encode(text_bytes)
    b64_decode_bytes = base64.b64decode(text_bytes)
    b64_message = b64_bytes.decode("ascii")
    plain_message = b64_decode_bytes.decode("ascii")
    print(f"Encoded Message: {b64_message}\nDecoded Message: {plain_message}")
    
def caesar(client, text):
    res = ""
    key = int(input("If you have one, please enter a key. Otherwise, enter 0: "))
    if key != 0:
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                res += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                res += chr((ord(char) + key - 97) % 26 + 97)
            else:
                res += char
            print(f"Processed Message: {res}")
        return
    strings = []
    for i in range(1, 27):
        for j in range(len(text)):
            if text[j].isupper():
                res += chr((ord(text[j]) + i - 65) % 26 + 65)
            elif text[j].islower():
                res += chr((ord(text[j]) + i - 97) % 26 + 97)
            else:
                res += text[j]
        print(f"Key: {i:<10} \t| Processed Message: {res:>10}")
        strings.append(res)
        res = ""
    ans = promptAi.promptAI(client, "You are given a list of Caesar Cipher results. Select the one that would make the most sense. Keep in mind this would usually be for a CTF. Keep responses short.", strings)
    print(ans)

def vigenere(text):
    def gen_key(text, key):
        ind = 0
        fixed = ""
        for char in text:
            if char.isalpha():
                fixed += key[ind % len(key)]
                ind+=1
            else:
                fixed += char
        return fixed
    
    key = input("Enter key: ")
    fixed_key = gen_key(text, key)
    enc_res, dec_res = [], []
        
    # encrypting loop
    for i in range(len(text)):
        # fix key character
        key_char = fixed_key[i].upper() if text[i].isupper() else fixed_key[i].lower()
        if text[i].isupper():
            enc_res.append(chr((ord(text[i]) + ord(key_char) - 2 * ord("A")) % 26 + ord("A")))
        elif text[i].islower():
            enc_res.append(chr((ord(text[i]) + ord(key_char) - 2 * ord("a")) % 26 + ord("a")))
        else:
            enc_res.append(text[i])
    print(f"Encrypted message: {"".join(enc_res)}")
    
    # decrypting loop 
    for i in range(len(text)):
        key_char = fixed_key[i].upper() if text[i].isupper() else fixed_key[i].lower()
        if text[i].isupper():
            dec_res.append(chr((ord(text[i]) - ord(key_char) + 26) % 26 + ord("A")))
        elif text[i].islower():
            dec_res.append(chr((ord(text[i]) - ord(key_char) + 26) % 26 + ord("a")))
        else:
            dec_res.append(text[i])
    print(f"Decrypted message: {"".join(dec_res)}")

def rsa():
    print("For all values, enter them if you have it. Otherwise, put in 0.")
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    n = int(input("Enter public key value (n): "))
    c = int(input("Enter ciphertext (c): "))
    e = int(input("Enter e (usually 65337): "))
    d = int(input("Enter private key (d): "))
    totient = int(input("Enter totient: "))
    m = int(input("Enter message text (m): "))
    
    if n == 0 and (p != 0 and q != 0):
        n = p * q
        print("N: " + n)
    elif p == 0 and (n != 0 and q != 0):
        p = n / q
        print("P: " + p)
    elif q == 0 and (n != 0 and p != 0):
        q = n / p
        print("Q: " + q)
    elif totient == 0 and (p != 0 and q != 0):
        totient = (p-1) * (q-1)
        print("Totient: " + totient)
import base64, os, time

def b64String(text):
    text_bytes = text.encode("ascii")
    b64_bytes = base64.b64encode(text_bytes)
    b64_decode_bytes = base64.b64decode(text_bytes)
    b64_message = b64_bytes.decode("ascii")
    plain_message = b64_decode_bytes.decode("ascii")
    print(f"Encoded Message: {b64_message}\nDecoded Message: {plain_message}")
    
def caesar(text):
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
            print(f"Encoded Message: {res}")
            return
        
    for i in range(1, 27):
        for j in range(len(text)):
            if text[j].isupper():
                res += chr((ord(text[j]) + i - 65) % 26 + 65)
            elif text[j].islower():
                res += chr((ord(text[j]) + i - 97) % 26 + 97)
            else:
                res += text[j]
        print(f"Key: {i} \t| Encoded Message: {res}")
        res = ""
            

def main():
    print("Welcome to DCrpt. Your all in one cryptography software. If input is supplied via file (binary data), please put it in and restart.\nPlease select the option you want to use.")
    choice = 0
    while choice != -1: 
        choice = int(input("1. Base64\n2. Caesar Cipher\n"))
        text = input("Please enter your text: ")
        if (choice > 2):
            print("Invalid Entry.")
        elif (choice == 1):
            b64String(text)
        elif (choice == 2):
            caesar(text)
        time.sleep(1)
    
    
if __name__ == "__main__":
    main()
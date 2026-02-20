from google import genai
from dotenv import load_dotenv
import os, time, methods


def main():
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    print("Welcome to DCrpt. Your all in one cryptography software.\nPlease select the option you want to use. To exit, enter -1.")
    choice = 0
    while choice != -1: 
        choice = int(input("1. Base64\n2. Caesar Cipher\n3. Vigenere Cipher\n4. RSA Decryption\n"))
        text = input("Please enter your text. If using RSA, you can skip this: ")
        if (choice > 4):
            print("Invalid Entry.")
        elif (choice == 1):
            methods.b64String(text)
        elif (choice == 2):
            methods.caesar(client, text)
        elif (choice == 3):
            methods.vigenere(text)
        elif (choice == 4):
            methods.rsa()
        time.sleep(1)
    
    
if __name__ == "__main__":
    main()
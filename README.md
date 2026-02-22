# Dcrpt
A small AI-powered encryption and decryption software built for CTFs. Contains base64, Vigenère, RSA, and Caesar ciphers.

## Contains:
1. Base64
2. Ceaesar Cipher
3. Vigenere
4. RSA Decryption

All ciphers (except RSA) will both encrypt and decrypt your text.

## To run:
1. Clone this repo!
2. In your terminal, set up a virtual environment using:
   - **python3 -m venv venv**
   - **source venv/bin/activate**
   - These commands are for linux, please look <a href="https://docs.python.org/3/library/venv.html">here</a> for other operating systems.
3. Then, run **pip install -r requirements.txt**
4. You do need to create your own API key for this, to do so:
   - Go to <a href="https://aistudio.google.com/">here</a> and click the **Get API key** button in the bottom left.
   - Create a .env file, and input the key as so: **GEMINI_API_KEY="PUT THE KEY IN THE QUOTES"**
6. Enjoy!

Please let me know if there are any issues, and I will (hopefully) fix them quickly.

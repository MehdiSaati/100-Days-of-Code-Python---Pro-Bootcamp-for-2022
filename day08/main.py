# Caesar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(art.logo)
while True:
    def encrypt(plain_text, shift_amount):
        cipher_text =""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 28:
               new_position -= 28
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encode text is : {cipher_text}\n")

    def decrypt(cipher_text, shift_amount):
        plain_text =""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            if new_position < 0:
               new_position += 28
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"The decode text is : {plain_text}\n")

    direction = input("Type 'encode' ro encrypt, type 'decode' to decrypt: \n").lower()
    shift = int(input("Type the shift number: \n"))
    text = input("Type your message: \n").lower()
    
    if direction == "encode":
        encrypt(plain_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt(cipher_text = text, shift_amount = shift)


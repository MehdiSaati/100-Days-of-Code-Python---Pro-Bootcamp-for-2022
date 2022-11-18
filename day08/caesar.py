# Single function Caesar Cipher
# Combine the encrypt() and decrypt function
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(art.logo)
while True:
    def caesar(start_text, shift_amount, cipher_direction):
        end_text =""
        for letter in start_text:
            position = alphabet.index(letter)
            if cipher_direction == "decode":
                shift_amount *= -1
            new_position = position + shift_amount
            end_text += alphabet[new_position]

        print(f"The {cipher_direction}d  text is : {end_text}\n")

    direction = input("Type 'encode' ro encrypt, type 'decode' to decrypt: \n").lower()
    shift = int(input("Type the shift number: \n"))
    text = input("Type your message: \n").lower()
 
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction )
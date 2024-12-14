alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = ''
while direction != 'encode' and direction != 'decode':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input('Type your message: ').lower()
shift = int(input('Type your shift number: '))

def encrypt(original_text=text, shift_amount=shift):
    encrypted_string = ''
    for letter in original_text:
        if letter == " ":
            encrypted_letter = " "
        elif alphabet.index(letter) + shift_amount < len(alphabet):
            encrypted_letter = alphabet[alphabet.index(letter) + shift_amount]
        else:
            encrypted_letter = alphabet[(alphabet.index(letter) + shift_amount) - len(alphabet)]
        encrypted_string += encrypted_letter
    print(encrypted_string)

def decrypt(original_text=text, shift_amount=shift):
    decrypted_string = ''
    for letter in original_text:
        if letter == " ":
            decrypted_letter = " "
        elif alphabet.index(letter) - shift_amount >= 0:
            decrypted_letter = alphabet[alphabet.index(letter) - shift_amount]
        else:
            decrypted_letter = alphabet[(alphabet.index(letter) - shift_amount) + len(alphabet)]
        decrypted_string += decrypted_letter
    print(decrypted_string)

if direction == 'encode':
    encrypt()
else:
    decrypt()
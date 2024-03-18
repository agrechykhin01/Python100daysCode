alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        new_letter_index = letter_index + shift
        if new_letter_index > (len(alphabet) - 1):
            new_letter_index = new_letter_index % len(alphabet)
        encrypted += alphabet[new_letter_index]
    print(f"The encoded text is: {encrypted}")

def decrypt(text, shift):
    decrypted = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        new_letter_index = letter_index - shift
        if new_letter_index < 0:
            new_letter_index = len(alphabet) - ((-(new_letter_index)) % (len(alphabet) - 1))
        decrypted += alphabet[new_letter_index]
    print(f"The decoded text is: {decrypted}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
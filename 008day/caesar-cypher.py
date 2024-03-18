alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    result_text = ""
    for letter in text:
        letter_index = alphabet.index(letter)

        if direction == "encode":
            new_letter_index = letter_index + shift
            result_text += alphabet[new_letter_index]
        elif direction == "decode":
            new_letter_index = letter_index - shift
            result_text += alphabet[new_letter_index]
        else:
            print("Type only 'encode' or 'decode' as direction!")

    print(f"The {direction}d text is: {result_text}")

caesar(text, shift, direction)
